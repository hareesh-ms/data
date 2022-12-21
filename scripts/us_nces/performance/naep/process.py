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
"""
This Python Script Load the datasets, cleans it
and generates cleaned CSV, MCF, TMCF file.
Before running this module, run download_input_files.py script, it downloads
required input files, creates necessary folders for processing.
Folder information
input_files - downloaded files (from nces naep website) are placed here
output_files - output files (mcf, tmcf and csv are written here)
"""

import os
import sys

from absl import app
from absl import flags
from absl import logging


MODULE_DIR = os.path.dirname(__file__)
sys.path.insert(1, MODULE_DIR + '/../../../statvar')
#pylint:disable=wrong-import-position
#pylint:disable=import-error
#pylint:disable=wildcard-import
from stat_var_processor import StatVarDataProcessor, process
#pylint:enable=wrong-import-position
#pylint:enable=import-error
#pylint:disable=wildcard-import


# pylint:disable=too-few-public-methods

_FLAGS = flags.FLAGS

class NaepEduPerformance(StatVarDataProcessor):
    """
    This is a subClass that inherits proeprties from StatVarDataProcessor.
    """
    _import_name = "naep"
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "input_files")
    
    '''
    input_files = [
        os.path.join(input_path, file)
        for file in sorted(os.listdir(input_path))
        if file != ".DS_Store"
    ]
    '''
if __name__ == '__main__':

    _input_files = ['/usr/local/google/home/hareeshms/Projects/datacommons/education/performance/repo/data/scripts/us_nces/performance/naep/input_files/naep_performance_input_bkp.csv']

    _output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "output_files")
    _conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "config")
    #_pv_map = os.path.join(_conf_path, 'pv_map.py')

    _pv_map = ['/usr/local/google/home/hareeshms/Projects/datacommons/education/performance/repo/data/scripts/us_nces/performance/naep/config/pv_map.py','jurisdiction:/usr/local/google/home/hareeshms/Projects/datacommons/education/performance/repo/data/scripts/us_nces/performance/naep/config/jurisdiction_map.py']

    #_config_file = os.path.join(_conf_path, 'pv_map.py')
    _config_file = '/usr/local/google/home/hareeshms/Projects/datacommons/education/performance/repo/data/scripts/us_nces/performance/naep/config/naep_config.py'

    process(data_processor_class=NaepEduPerformance,
                        input_data=_input_files,
                        output_path=_output_path,
                        config_file=_config_file,
                        pv_map_files=_pv_map)


# pylint:enable=too-few-public-methods
