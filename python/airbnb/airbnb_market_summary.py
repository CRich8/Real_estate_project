import requests
import pandas as pd
import json

url = "https://mashvisor-api.p.rapidapi.com/airbnb-property/market-summary"

querystring = {"state":"NJ","city":"Hoboken"}

headers = {
	"X-RapidAPI-Key": "0b52c0e7fcmshaed8f0f998397c0p182f41jsn7900be6276c2",
	"X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()

data = data['content']
df = pd.json_normalize(data)
print(df)
property_types = df['property_types.histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index')
occupancy_histogram = df['occupancy_histogram.histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index')
night_price_histogram = df['night_price_histogram.histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index')
rental_income_histogram = df['rental_income_histogram.histogram'].apply(pd.Series).reset_index().melt(id_vars='index').dropna()[['index', 'value']].set_index('index')

frames = [property_types,occupancy_histogram,night_price_histogram,rental_income_histogram]
df_final = pd.concat(frames, axis=1)
df_final.columns = ['property_types','occupancy','night_price','rental_income']

result = df_final.to_csv('hoboken_market_summary2.csv',index=False)

