# Assignment 1 - Task 1 - Pre-processing

import pandas as pd
import numpy as np
import datetime


def getData(filename):
	return pd.read_csv(filename, error_bad_lines=False, sep=',', encoding='latin-1')

mood_smartphones = getData('dataset_mood_smartphone.csv')

# Create table for missing data analysis
def draw_missing_data_table(df):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    return missing_data

draw_missing_data_table(mood_smartphones)


mood_smartphones['variable'].unique()


# Convert dates to pd Timestamps/datetime
mood_smartphones['time'] = pd.to_datetime(mood_smartphones['time'], format='%Y-%m-%d %H:%M:%S.%f')
cutoff = pd.Timestamp(year=2014, month=2, day=28)

# Print data until cutoff for subject 1
print("Cutoff selection: ", cutoff)
print(mood_smartphones[(mood_smartphones["id"] == "AS14.01") & (mood_smartphones['time'] < cutoff)])
