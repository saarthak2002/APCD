import pandas as pd
data = pd.read_csv('/project/biocomplexity/anil/APCD/saarthak/extracted_data_csv/yearly/2019.csv')

VAzipcodes = pd.read_csv('csvData.csv')
zips=VAzipcodes['zip'].unique()

column_names = ["zipcode", "member_count"]
countDF = pd.DataFrame(columns = column_names)

for z in zips:
    l=len(data.loc[data['Member Zip Code DOS']==z]['MI Person Key'].unique())
    print(z,l)
    df2 = {'zipcode': z, 'member_count': l}
    countDF = countDF.append(df2, ignore_index = True)

countDF.to_csv("2019_member_count.csv");