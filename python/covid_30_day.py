import pandas as pd
from datetime import timedelta
path = '/project/biocomplexity/anil/APCD/saarthak/extracted_data_csv/'
antiDir = pd.read_csv(path+'antibiotic_directory.csv', index_col=0)
covidPatients = pd.read_csv(path+'1_covid_patients_with_demo_and_1st_covid_incurred_data.csv')

antiDir['IncurredTimeStamp'] = pd.to_datetime(antiDir['Incurred Date'], format='%Y%m%d')
covidPatients['IncurredTimeStamp'] = pd.to_datetime(covidPatients['1st_incurred_date'], format='%Y%m%d')

g = 0
to_app = []
for index, row in covidPatients.iterrows():
    person = row['mi_person_key'] #get MI Key of that person
    covidDate = row['IncurredTimeStamp'] #get covid time stamp
    all_claims_for_person = antiDir[antiDir['MI Person Key'] == person] #get datafarme of all antibiotic claims for that person
    all_claims_dates_list = all_claims_for_person['IncurredTimeStamp'].tolist() #get list of all claim timestamps for that person
    
    if not all_claims_dates_list: #if person has no antibiotic claims ever
        to_app.append(row) #add person to data
        continue
        
    validPatient = True
    earliest_date_of_30_day_range = covidDate - timedelta(days=30)
    latest_date_of_20_day_range = covidDate + timedelta(days=20)
    
    for claim_date in all_claims_dates_list: #check if patient has antibiotic history in last 30 days
        if(claim_date <= covidDate and claim_date >= earliest_date_of_30_day_range): #person has antibiotics history in last 30 days
            validPatient = False
            break
    
    if(validPatient): #Patient has no antibiotic histoy in last 30 days
        for claim_date in all_claims_dates_list:
            if(claim_date >= covidDate and claim_date <= latest_date_of_20_day_range): # covidDate <= claim_date <= covidDate+20 : if person has anti in 20 days of covid
                to_app.append(row)

df = pd.DataFrame(to_app)
df.to_csv('range_30_20_covid_patients.csv')