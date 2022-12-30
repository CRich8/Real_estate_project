import requests
import pandas as pd
import json

url = "https://mashvisor-api.p.rapidapi.com/rental-rates"

querystring = {"state":"NJ","city":"Hoboken","source":"airbnb"}

headers = {
	"X-RapidAPI-Key": "0b52c0e7fcmshaed8f0f998397c0p182f41jsn7900be6276c2",
	"X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()

data = data['content']

list = []
for data_item in data['detailed']:
    list.append(data_item)
df_detailes = pd.DataFrame(list)

rates_data = data['retnal_rates']
df_keys = pd.DataFrame.from_dict(rates_data.keys())
df_keys.columns =['room_size']
df_values = pd.DataFrame.from_dict(rates_data.values())
df_values.columns =['value']

frames = [df_keys,df_values,df_detailes]

df_final = pd.concat(frames,axis=1)

result = df_final.to_csv('hoboken_rental_rates2.csv',index=False)

