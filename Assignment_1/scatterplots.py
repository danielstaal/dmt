# Assignment 1 - Task 1 - Pre-processing

import pandas as pd
import numpy as np
import datetime
import traces
import matplotlib.pyplot as plt
# plt.style.use('fivethirtyeight') 
import dateutil
from matplotlib.patches import Rectangle

def getData(filename):
	return pd.read_csv(filename, error_bad_lines=False, sep=',', encoding='latin-1')

# Create table for missing data analysis
def draw_missing_data_table(df):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    return missing_data

def getSubset(dataframe, start, end, subjectid):
	return dataframe[(dataframe["id"] == subjectid) & (dataframe['time'] < end) & (dataframe['time'] > start)]

def allSubjects(dataframe):
    return dataframe['id'].unique()
# if __name__ == "__main__":
# Get data
mood = getData('dataset_mood_smartphone.csv')

# convert dates to pd Timestamps/datetime
mood['time'] = pd.to_datetime(mood['time'], format='%Y-%m-%d %H:%M:%S.%f')
# draw_missing_data_table(mood)
# mood['variable'].unique()

# date ranges
start = pd.Timestamp(year=2014, month=3, day=1)
cutoff = pd.Timestamp(year=2014, month=5, day=30)

sub1 = getSubset(mood, start, cutoff, "AS14.01")
sub2 = getSubset(mood, start, cutoff, "AS14.02")
moodsub1 = sub1[(sub1['variable'] == 'mood')]


testtime = traces.TimeSeries()
for idx, row in moodsub1.iterrows():
    testtime[row['time']] = row['value']
print(testtime)
# print(testtime[datetime.datetime(2014, 3, 25, 20,  30, 0)])
transformed = testtime.moving_average(3000, pandas=True)
# print(transformed)
# plt.plot(transformed)
# plt.scatter(moodsub1['time'], moodsub1['value'])
# plt.show()

globmin = mood['time'].min()
globmax = mood['time'].max()

subjectCounts = {}
for subject in allSubjects(mood):
    start = mood['time'][(mood['id'] == subject)].min()
    cutoff = mood['time'][(mood['id'] == subject)].max()
    subset = getSubset(mood, start, cutoff, subject)
    # print("\n\n\nSTATS FOR:", subject,"\n")
    variables = subset['variable'].unique()
    subjectdict = {}
    handles = []
    strings = []
    for var in variables:
        subjectdict[var] = len(subset[(subset['variable'] == var)])
        # print("length of", var, "=", len(subset[(subset['variable'] == var)]))
        handles.append(Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0))
        strings.append(var + ": " + str(subjectdict[var]))

    subjectCounts[subject] = subjectdict
    
    # # Uncomment for scatterplots
    plt.figure(figsize=(16,8))
    plt.title(subject)
    plt.scatter(subset['time'], subset['variable'], s = 1, label=subjectCounts[subject])
    plt.xlim(left = start, right=cutoff)
    plt.tight_layout()
    
    plt.legend(reversed(handles),reversed(strings),loc=0,framealpha=0.35)
    plt.savefig(subject+".png")
    plt.close()
    # plt.show()
print(subjectCounts["AS14.01"])