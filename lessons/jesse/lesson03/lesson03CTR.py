#lesson03 CTR

from numpy import *
import pandas as pd


for csv in range(1,3)
	r = reg.get (‘http://stat.columbia.edu/~rachel/datasets/nyt’ + csv + ‘.csv’)
	r.text
	df = df.append(pd.read_csv(r.text)))

df.to_csv('nytimes_aggregation.csv')

df['Clicks'].astype(float64)

df['CTR'] = df['Clicks']/df['Impressions']
df[:10]



dfg1 = df[ ['Age', 'CTR'] ].groupby(['Age']).agg([sum])
dfg1[:20]

dfg2 = df[ ['Gender', 'CTR'] ].groupby(['Gender']).agg([sum])
dfg2[:20]

dfg3 = df[ ['Signed_In', 'CTR'] ].groupby(['Signed_In']).agg([sum])
dfg3[:20]

