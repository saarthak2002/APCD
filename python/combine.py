import pandas as pd
import numpy as np
import glob
import os
path='/project/biocomplexity/anil/APCD/saarthak/extracted_data_csv/UVA_prescriptions_2016/'
all_files = glob.glob(os.path.join(path, "*.csv"))
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
df = df.drop(columns=df.columns[0])
df.to_csv('/project/biocomplexity/anil/APCD/saarthak/extracted_data_csv/yearly/2016.csv',index=False)