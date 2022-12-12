import pandas as pd
import csv 

df = pd.read_csv('total_stars.csv')
print(df.shape)
print(list(df))

df.drop(['Unnamed: 0', 'Luminosity', 'Unnamed: 6',  'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'], axis = 1, inplace=True)
print(list(df))


final_data = df.dropna()
final_data.to_csv('final_data.csv')