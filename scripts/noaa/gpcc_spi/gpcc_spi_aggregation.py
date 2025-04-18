# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd
import json
from datetime import datetime
import os
import glob
from pathlib import Path

from absl import flags
from absl import app
from absl import logging

_SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
FLAGS = flags.FLAGS

flags.DEFINE_string(
    'gpcc_spi_preprocessed_pattern', 'output_files/*.csv',
    'The directory the csvs generated by preprocess_gpcc_spi.py')

DEFAULT_PLACE_AREA_RATIO_JSON_PATH = os.path.join(
    os.path.dirname(__file__), 'geojson_data/place_area_ratio.json')
flags.DEFINE_string('place_area_ratio_json_path',
                    DEFAULT_PLACE_AREA_RATIO_JSON_PATH,
                    'Path to place area json cache.')
default_output_path = os.path.join(
    _SCRIPT_PATH,
    "output_files/aggregations",
)
flags.DEFINE_string('gpcc_spi_agg_dir', default_output_path,
                    'The directory where the output mcf will be generated in.')


def get_place_grid_ratio_dict(path):
    """Returns place area json mapping from path."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


# TODO(alexyfchen): Improve with df operations rather than loop.
def aggregate_with_loop(agg_dir, place_grid_ratio_dict, spi_df, period):
    """Loop over resolved places and aggregate spi for each place."""
    path = os.path.join(agg_dir, f'agg_gpcc_spi_pearson_{period}.csv')
    if os.path.isfile(path):
        os.remove(path)

    columns = [
        'place', 'time', 'variable', 'period', 'spi', 'observationPeriod'
    ]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(','.join(columns) + '\n')

    for place_id, grids in place_grid_ratio_dict.items():
        # Find all spis relevant to the grids
        relevant_spis = spi_df.loc[spi_df['grid_key'].isin(
            [g["grid"] for g in grids])]
        if len(relevant_spis) == 0:
            continue

        place_df = pd.DataFrame([[g['grid'], g['ratio']] for g in grids],
                                columns=['grid_key', 'ratio'])
        place_df.set_index('grid_key')

        merged = relevant_spis.merge(place_df)
        merged['spi'] = merged['spi'] * merged['ratio']

        weighted = merged.groupby('time').agg('sum')

        filtered = weighted.loc[weighted['ratio'] > 0.999].reset_index()

        time_weighted_spi = filtered.drop('ratio', axis=1)
        time_weighted_spi['place'] = place_id
        time_weighted_spi['period'] = f'"[{int(period)} dcs:Monthly]"'
        time_weighted_spi['observationPeriod'] = f'P{int(period)}M'
        time_weighted_spi[
            'variable'] = f'dcs:StandardizedPrecipitationIndex_Atmosphere_{int(period)}MonthPeriod'

        time_weighted_spi.to_csv(path,
                                 columns=columns,
                                 header=False,
                                 mode='a',
                                 index=False,
                                 quotechar="'")
    return path


def _read_spi_data_csv(csv_path):

    def grid_to_coord(grid):
        """grid_1/lat_lng -> lat^lng"""
        lat_lng = grid.split('/')[1]
        return "^".join(lat_lng.split('_'))

    df = pd.read_csv(csv_path, usecols=['time', 'place', 'spi'])
    df['grid_key'] = df['place'].map(grid_to_coord)
    df.drop('place', axis=1)
    df.set_index('grid_key')
    return df


def run_gpcc_spi_aggregation(in_pattern, agg_dir,
                             place_area_ratio_json_path: str):
    """Run aggregates from one degree grid csvs and return a mapping of agg paths."""
    place_grid_ratio = get_place_grid_ratio_dict(place_area_ratio_json_path)
    logging.info('finished reading grid ratio df %s',
                 datetime.now().strftime("%H:%M:%S"))

    os.makedirs(agg_dir, exist_ok=True)

    output_paths = dict()
    full_pattern = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                in_pattern)
    for file in sorted(glob.glob(full_pattern)):
        path = Path(file)
        period = path.stem.split('_')[-1]

        spi_df = _read_spi_data_csv(file)
        logging.info('finished reading spi df %s:  %s', file,
                     datetime.now().strftime("%H:%M:%S"))

        output_path = aggregate_with_loop(agg_dir, place_grid_ratio, spi_df,
                                          period)
        logging.info('finished agg for %s: %s', file,
                     datetime.now().strftime("%H:%M:%S"))

        output_paths[str(path)] = output_path

    return output_paths


def main(_):
    """Run aggretation with flag values."""
    run_gpcc_spi_aggregation(FLAGS.gpcc_spi_preprocessed_pattern,
                             FLAGS.gpcc_spi_agg_dir,
                             FLAGS.place_area_ratio_json_path)


if __name__ == "__main__":
    app.run(main)
