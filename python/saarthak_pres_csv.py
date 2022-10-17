import pandas as pd
import sys
import os
import json

infile = sys.argv[1]
outfile = sys.argv[2]

df = pd.read_csv(infile, sep = "|", dtype='object')
df['Month'] = df["Incurred Date"].astype(str).str[:6].astype(int)

prescriptions = {}
p = df.loc[:,["Incurred Date",
              "MI Person Key",
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
p.to_csv("{}.csv".format(outfile))



