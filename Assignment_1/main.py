# Assignment 1 - Task 1 - Pre-processing

import pandas as pd
import numpy as np
import datetime

def getData(filename):
	return pd.read_csv(filename, error_bad_lines=False, sep=',', encoding='latin-1')

# Create table for missing data analysis
def draw_missing_data_table(df):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    return missing_data

def getSubset(dataframe, start, end, subjectid):
'''
Get data for subjectid in time range (start - end (timestamps)) 	
'''	
	return dataframe[(dataframe["id"] == subjectid) & (dataframe['time'] < end) & (dataframe['time'] > start)]



# Get data
mood_smartphones = getData('dataset_mood_smartphone.csv')
draw_missing_data_table(mood_smartphones)
mood_smartphones['variable'].unique()

# Convert dates to pd Timestamps/datetime
mood_smartphones['time'] = pd.to_datetime(mood_smartphones['time'], format='%Y-%m-%d %H:%M:%S.%f')

# Print data until cutoff for subject 1
start = pd.Timestamp(year=2014, month=3, day=20)
cutoff = pd.Timestamp(year=2014, month=3, day=29)

print(getSubset(mood_smartphones, start, cutoff, "AS14.01")