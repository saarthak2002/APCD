import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
from pathlib import Path
import json


data = pd.read_csv('all_antibiotics')
VAzipcodes = pd.read_csv('csvData.csv')


column_names = ["zipcode", "month", "count"]
countDF = pd.DataFrame(columns = column_names)

months = data['Month'].unique()
for zipcode in VAzipcodes['zip']:
    for month in months:
        count = len(data.loc[(data['Month']==month) & (data['Member Zip Code DOS']==zipcode)].index)
        df2 = {'zipcode': zipcode, 'month': month, 'count': count}
        countDF = countDF.append(df2, ignore_index = True)

countDF.to_csv('zipcodeMemberPresCount.csv')