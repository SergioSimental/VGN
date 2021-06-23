import requests
import json
from datetime import date

DATE = date.today()
API_KEY = '91bbdf9adfeb4c0f8e046fb4e1e58933'

# Save data to json file - rewrite: deletes old data
def save(data):
    with open('data.json', 'w') as fp:
        json.dump(data, fp)


# Update data to json file - append: adds to old data
def update(data):
    temp_data = None
    with open('data.json', 'r+') as fp:
        d = json.load(fp)
        temp_data = d
        save(data)

    with open('data.json', 'r+') as fp:   
        n = json.load(fp)
        n.update(temp_data)
        fp.seek(0)
        json.dump(n, fp)

# Script to update news articles data from New API
url = f'https://newsapi.org/v2/everything?q=gaming&from={DATE}&sortBy=popularity&language=en&apiKey={API_KEY}'
response = requests.get(url)
data = response.json()
update(data)



