import pandas as pd

dataPath = '/project/biocomplexity/anil/APCD/saarthak/extracted_data_csv/all.csv'

all_dat = pd.read_csv(dataPath)
all_dat['Month'] = all_dat['Month'].astype(str)
all_dat['Year']  = all_dat.Month.str[:4]
all_dat_race = all_dat.groupby(['Year','Member Race']).count()
all_dat_race = all_dat_race.filter(['Year', 'Member Race','MI Person Key'])

all_dat_race.to_csv('all_member_race_year.csv')