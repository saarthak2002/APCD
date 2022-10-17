import pandas as pd
import sys
import os
import json

infile = sys.argv[1]
outfile = sys.argv[2]

df = pd.read_csv(infile, sep = "|", dtype='object')
df['Month'] = df["Incurred Date"].astype(str).str[:6].astype(int)

prescriptions = {}
p = df.loc[:,["MI Person Key",
              "Payer Type",
              "Member Age DOS",
              "Month",
              "Drug Code",
              "GPI",
              "Drug Name",
              "Strength",
              "Member Zip Code DOS",
              "Member County DOS",
              "Service Provider ZIP",
              "Service Provider County",
              "Member Gender",
              "Member Race",
              "Hispanic Indicator"]]


p.rename(columns = {"Drug Code": "NDC"}, inplace = True)
p.replace({"Unknown": None, "Unkno": None, "Unspecified": None}, inplace = True)
grouped = p.groupby(by = ["NDC"], dropna=False)

for drug, frame in grouped:
    if drug in prescriptions.keys():
        prescriptions[drug] = pd.concat([prescriptions[drug], frame], ignore_index = True)
    else:
        prescriptions[drug] = frame.reset_index(drop = True)
for key in prescriptions:
    prescriptions[key] = prescriptions[key].to_dict()
with open(outfile, "w") as f:
    json.dump(prescriptions, f)



