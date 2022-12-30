import requests
import pandas as pd
import json

url = "https://mashvisor-api.p.rapidapi.com/airbnb-property/occupancy-rates"

querystring = {"state":"NJ","city":"Hoboken"}

headers = {
	"X-RapidAPI-Key": "0b52c0e7fcmshaed8f0f998397c0p182f41jsn7900be6276c2",
	"X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()

data = data['content']
df = pd.json_normalize(data)

detailed_studio_occupancies = df['detailed.studio_occupancies_histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index').reset_index(drop=True)
detailed_one_bedroom = df['detailed.one_bedroom_histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index').reset_index(drop=True)
detailed_two_bedrooms = df['detailed.two_bedrooms_histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index').reset_index(drop=True)
detailed_three_bedrooms = df['detailed.three_bedrooms_histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index').reset_index(drop=True)
detailed_four_bedrooms = df['detailed.four_bedrooms_histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index').reset_index(drop=True)

df_occupancy = df[['occupancy_rates.studio','occupancy_rates.one_bedroom','occupancy_rates.two_bedrooms','occupancy_rates.three_bedrooms','occupancy_rates.four_bedrooms']]

df = df.reset_index(drop=True)
frames = [df_occupancy,detailed_studio_occupancies,detailed_one_bedroom,detailed_two_bedrooms,detailed_three_bedrooms,detailed_four_bedrooms]
df_final = pd.concat(frames,axis=1)
df_final.columns = ['occupancy_rates_studio','occupancy_rates_one_bedroom','occupancy_rates_two_bedrooms','occupancy_rates_three_bedrooms','occupancy_rates_four_bedrooms','detailed_studio_occupancies','detailed_one_bedroom','detailed_two_bedrooms','detailed_three_bedrooms','detailed_four_bedrooms']

result = df_final.to_csv('hoboken_occupancy_rates2.csv',index=False)

