import pandas as pd
import networkx as nx
from datetime import timedelta

G = nx.Graph()
claims = pd.read_csv('/project/biocomplexity/anil/APCD/saarthak/code/MRSA_patients_with_broad_facility.csv')
claims = claims[claims['Member Zip Code DOS'].notna()]
claims = claims[claims['Broad Categories'].notna()]

zips = claims['Member Zip Code DOS'].unique()
fac_type = claims['Broad Categories'].unique()

#Add nodes of type (zipcode, facility) to the network
i = 0
for z in zips:
    for fac in fac_type:
        if fac == None:
            continue
        G.add_node(i, zipcode=z,facility_type=fac)
        i=i+1
        
unique_patient_ids = claims['MI Person Key'].unique()

#add edges
for pat_id in unique_patient_ids:
    patient_claims = claims.loc[claims['MI Person Key'] == pat_id]
    patient_claims = patient_claims.sort_values(by='Incurred Date TS')
    
    dates = patient_claims['Incurred Date TS'].to_numpy()
    zipcodes = patient_claims['Member Zip Code DOS'].to_numpy()
    facilities = patient_claims['Broad Categories'].to_numpy()
    
    for i in range(0,len(zipcodes)-1):
        try:
            zipcode1 = zipcodes[i]
            fac1 = facilities[i]
            zipcode2 = zipcodes[i+1]
            fac2 = facilities[i+1]

            date1 = pd.to_datetime(dates[i], format='%Y-%m-%d')
            date2 = pd.to_datetime(dates[i+1], format='%Y-%m-%d')
            futureDate = date1 + timedelta(days=7)

            if (date1 <= date2 and date2 <= futureDate): #if second claim is within 7 days of first claim
                if zipcode1 != zipcode2: #patients who were transfered to a different zipcode
                    node1 = [x for x,y in G.nodes(data=True) if (y['zipcode'] == zipcode1 and y['facility_type'] == fac1)][0]
                    node2 = [x for x,y in G.nodes(data=True) if (y['zipcode'] == zipcode2 and y['facility_type'] == fac2)][0]
                    G.add_edge(node1,node2)
                if ((zipcode1 == zipcode2) and (fac1 != fac2)): #patients who were transfered to another facility in the same zipcode
                    node1 = [x for x,y in G.nodes(data=True) if (y['zipcode'] == zipcode1 and y['facility_type'] == fac1)][0]
                    node2 = [x for x,y in G.nodes(data=True) if (y['zipcode'] == zipcode2 and y['facility_type'] == fac2)][0]
                    G.add_edge(node1,node2)
        
        except:
            continue

G.remove_nodes_from(list(nx.isolates(G)))
nx.write_gpickle(G,'transfer.gpickle')