
import pandas as pd

data = pd.read_csv('data/CRDC2013_14.csv', encoding='Latin-1')

#print(data['JJ'].value_counts())
#print(data['SCH_STATUS_MAGNET'].value_counts())

tb1 = data.pivot_table(index='JJ', values=['TOT_ENR_M', 'TOT_ENR_F'], aggfunc='sum')
tb2 = data.pivot_table(index='SCH_STATUS_MAGNET', values=['TOT_ENR_M', 'TOT_ENR_F'], aggfunc='sum')

print(tb1)
print(tb2)