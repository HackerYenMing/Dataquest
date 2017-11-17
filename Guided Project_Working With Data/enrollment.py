
import pandas as pd
import re

data = pd.read_csv('data/CRDC2013_14.csv', encoding='Latin-1')

data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']

data_cols = data.columns.tolist()
schENR_cols = []

for col in data_cols :
    if re.match('SCH_ENR', col) is not None :
        schENR_cols.append(col)

schENR_cols = schENR_cols[0:14]
#print(data[schENR_cols].sum())
        
all_enrollment = data['total_enrollment'].sum()
print(data[schENR_cols].sum() / all_enrollment)
