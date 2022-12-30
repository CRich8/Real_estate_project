import requests
import pandas as pd
import json

url = "https://mashvisor-api.p.rapidapi.com/airbnb-property/active-listings"

querystring = {"state":"NJ","city":"Hoboken","source":"airbnb"}

headers = {
	"X-RapidAPI-Key": "0b52c0e7fcmshaed8f0f998397c0p182f41jsn7900be6276c2",
	"X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()

data = data['content']

list = []
for data_item in data['properties']:
    list.append(data_item)
df = pd.DataFrame(list)
result = df.to_csv('hoboken_listings2.csv',index=False)

