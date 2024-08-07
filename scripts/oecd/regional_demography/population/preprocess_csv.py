# Copyright 2020 Google LLC
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

import sys

sys.path.append('../')
from utils import multi_index_to_single_index
import csv
import json
import pandas as pd

# Prod REGION_DEMOGR_population.csv is stored at
# https://pantheon.corp.google.com/storage/browser/_details/datcom-source-data/oecd/regional_demography/population/REGION_DEMOGR_population.csv?authuser=0&project=datcom-204919.
# Copy it over before running preprocess_csv:
# gsutil cp gs://datcom-source-data/oecd/regional_demography/population/REGION_DEMOGR_population.csv

# Process the dataset.
ag_df = []
df1 = pd.read_csv("REGION_DEMOGR_population.csv",
                  sep='\t',
                  low_memory=False,
                  index_col=None,
                  header=0)
# See README for how manual_curated_population is generated.
df2 = pd.read_csv("manual_curated_population.csv", index_col=None, header=0)
ag_df.append(df1)
ag_df.append(df2)
df = pd.concat(ag_df, axis=0, ignore_index=True)

# There can be AVG for national average, here we only care stats for Total Regions.
df = df[df['POS'] == 'ALL']
# Filter TL like "1_MR-L"(Country - Large metro TL3 regions)m "1_NMR-R"(Country - Remote TL3 regions).
df = df[df['TL'].isin(['1', '2', '3'])]
df = df[['TL', 'REG_ID', 'Region', 'VAR', 'SEX', 'Year', 'Value']]
# First remove geos with names that we don't have mappings to dcid for.
regid2dcid = dict(json.loads(open('../regid2dcid.json').read()))
df = df[df['REG_ID'].isin(regid2dcid.keys())]
# Second, replace the names with dcids
df['Region'] = df.apply(lambda row: regid2dcid[row['REG_ID']], axis=1)

df['Year'] = '"' + df['Year'].astype(str) + '"'

df_cleaned = df.pivot_table(values='Value',
                            index=['REG_ID', 'Region', 'Year'],
                            columns=['VAR', 'SEX'])
df_cleaned = multi_index_to_single_index(df_cleaned)

VAR_to_statsvars = {
    'TT': 'Count_Person',
    'Y0_4T': 'Count_Person_Upto4Years',
    'Y5_9T': 'Count_Person_5To9Years',
    'Y10_14T': 'Count_Person_10To14Years',
    'Y15_19T': 'Count_Person_15To19Years',
    'Y20_24T': 'Count_Person_20To24Years',
    'Y25_29T': 'Count_Person_25To29Years',
    'Y30_34T': 'Count_Person_30To34Years',
    'Y35_39T': 'Count_Person_35To39Years',
    'Y40_44T': 'Count_Person_40To44Years',
    'Y45_49T': 'Count_Person_45To49Years',
    'Y50_54T': 'Count_Person_50To54Years',
    'Y55_59T': 'Count_Person_55To59Years',
    'Y60_64T': 'Count_Person_60To64Years',
    'Y65_69T': 'Count_Person_65To69Years',
    'Y70_74T': 'Count_Person_70To74Years',
    'Y75_79T': 'Count_Person_75To79Years',
    'Y80_MAXT': 'Count_Person_80OrMoreYears',
    'Y0_14T': 'Count_Person_Upto14Years',
    'Y15_64T': 'Count_Person_15To64Years',
    'Y65_MAXT': 'Count_Person_65OrMoreYears',
    'TM': 'Count_Person_Male',
    'Y0_4M': 'Count_Person_Upto4Years_Male',
    'Y5_9M': 'Count_Person_5To9Years_Male',
    'Y10_14M': 'Count_Person_10To14Years_Male',
    'Y15_19M': 'Count_Person_15To19Years_Male',
    'Y20_24M': 'Count_Person_20To24Years_Male',
    'Y25_29M': 'Count_Person_25To29Years_Male',
    'Y30_34M': 'Count_Person_30To34Years_Male',
    'Y35_39M': 'Count_Person_35To39Years_Male',
    'Y40_44M': 'Count_Person_40To44Years_Male',
    'Y45_49M': 'Count_Person_45To49Years_Male',
    'Y50_54M': 'Count_Person_50To54Years_Male',
    'Y55_59M': 'Count_Person_55To59Years_Male',
    'Y60_64M': 'Count_Person_60To64Years_Male',
    'Y65_69M': 'Count_Person_65To69Years_Male',
    'Y70_74M': 'Count_Person_70To74Years_Male',
    'Y75_79M': 'Count_Person_75To79Years_Male',
    'Y80_MAXM': 'Count_Person_80OrMoreYears_Male',
    'Y0_14M': 'Count_Person_Upto14Years_Male',
    'Y15_64M': 'Count_Person_15To64Years_Male',
    'Y65_MAXM': 'Count_Person_65OrMoreYears_Male',
    'TF': 'Count_Person_Female',
    'Y0_4F': 'Count_Person_Upto4Years_Female',
    'Y5_9F': 'Count_Person_5To9Years_Female',
    'Y10_14F': 'Count_Person_10To14Years_Female',
    'Y15_19F': 'Count_Person_15To19Years_Female',
    'Y20_24F': 'Count_Person_20To24Years_Female',
    'Y25_29F': 'Count_Person_25To29Years_Female',
    'Y30_34F': 'Count_Person_30To34Years_Female',
    'Y35_39F': 'Count_Person_35To39Years_Female',
    'Y40_44F': 'Count_Person_40To44Years_Female',
    'Y45_49F': 'Count_Person_45To49Years_Female',
    'Y50_54F': 'Count_Person_50To54Years_Female',
    'Y55_59F': 'Count_Person_55To59Years_Female',
    'Y60_64F': 'Count_Person_60To64Years_Female',
    'Y65_69F': 'Count_Person_65To69Years_Female',
    'Y70_74F': 'Count_Person_70To74Years_Female',
    'Y75_79F': 'Count_Person_75To79Years_Female',
    'Y80_MAXF': 'Count_Person_80OrMoreYears_Female',
    'Y0_14F': 'Count_Person_Upto14Years_Female',
    'Y15_64F': 'Count_Person_15To64Years_Female',
    'Y65_MAXF': 'Count_Person_65OrMoreYears_Female',
}

df_cleaned.rename(columns=VAR_to_statsvars, inplace=True)

# Drop columns that are not related with populations.
drop_cols = []
csv_columns = {'REG_ID', 'Region', 'Year'}
csv_columns.update(VAR_to_statsvars.values())
for col in df_cleaned.columns:
    if col not in csv_columns:
        drop_cols.append(col)
df_cleaned.drop(columns=drop_cols, axis=0, inplace=True)

df_cleaned.to_csv('OECD_population_cleaned.csv',
                  index=False,
                  quoting=csv.QUOTE_NONE)

# Automate Template MCF generation since there are many Statitical Variables.
TEMPLATE_MCF_TEMPLATE = """
Node: E:OECD_population_cleaned->E{index}
typeOf: dcs:StatVarObservation
variableMeasured: dcs:{stat_var}
measurementMethod: dcs:OECDRegionalStatistics
observationAbout: C:OECD_population_cleaned->Region
observationDate: C:OECD_population_cleaned->Year
observationPeriod: "P1Y"
value: C:OECD_population_cleaned->{stat_var}
"""

stat_vars = df_cleaned.columns[3:]
with open('OECD_population.tmcf', 'w', newline='') as f_out:
    for i in range(len(stat_vars)):
        f_out.write(
            TEMPLATE_MCF_TEMPLATE.format_map({
                'index': i + 1,
                'stat_var': stat_vars[i]
            }))
