
import pandas as pd
import re

data = pd.read_csv('data/CRDC2013_14.csv', encoding='Latin-1')

data_cols = data.columns.tolist()
expulsion_cols = []

for col in data_cols :
    if re.match('SCH_DISCWODIS_EXPWOE_.+_M', col) is not None :
        expulsion_cols.append(col)

expulsion_M = data['TOT_DISCWODIS_EXPZT_M'].sum()
print(data[expulsion_cols].sum() / expulsion_M)
print('SUM :', expulsion_M)
