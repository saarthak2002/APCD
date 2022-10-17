import pandas as pd
import numpy as np
from pathlib import Path
import json

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

f = open('APCD/APCD/jainam/antibiotics_bii/filtered_antibiotics/all_antibiotics.json')
data = json.load(f)

import pandas

for month in data.keys():
    appended_data = []
    print("processing {}".format(month))
    for key in data[month].keys():
        dfOfCurrentNDCCode = pd.DataFrame.from_dict(data[month][key])
        appended_data.append(dfOfCurrentNDCCode)

    outfilename = "results/antibiotics{}.csv".format(month)
    appended_data = pd.concat(appended_data)
    appended_data.to_csv(outfilename)
    print("done processing {}".format(month))