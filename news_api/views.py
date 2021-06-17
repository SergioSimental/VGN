from django.shortcuts import render
import requests
from datetime import date
import json
from pathlib import Path

API_KEY = '91bbdf9adfeb4c0f8e046fb4e1e58933'
DATE = date.today()
file = '/newsapp/news_api/news.json'
json_news = { }


if Path('news.json').is_file():
    print ("File exist")
else:
    print ("File not exist")
    with open('news.json', 'w') as outfile:
        json.dump(json_news, outfile)


# Create your views here.

def home(request):
    url = f'https://newsapi.org/v2/everything?q=gaming&from={DATE}&sortBy=popularity&language=en&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    write_json(data,file)


    ds = json.loads(file)
    unique_news = { each['obj_id'] : each for each in ds}.values()

    articles = data['articles']
    
    context ={
	    'articles' : articles
    }

    return render(request, 'news/home.html', context)

def archive(request):
    url = f'https://newsapi.org/v2/everything?q=gaming&from={DATE}&sortBy=popularity&language=en&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    json_news.update(data)

    articles = json_news['articles']

    context={
        'articles' : articles
    }

    return render(request, 'news/archive.html', context)

    
def search(request):
    q = request.GET['query']
    url = f'https://newsapi.org/v2/everything?q=gaming&q={q}&sortBy=popularity&language=en&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articles= data['articles']

    context={
        'articles' : articles
    }    

    return render(request, 'news/search.html', context)



def write_json(new_data, file_name):
    with open(file, 'r+') as news:
        # First we load existing data into a dict.
        file_data = json.load(file_name)
        # Join new_data with file_data
        file_data.update(new_data)
        # Sets file's current position at offset.
        file_name.seek(0)
        # convert back to json.
        json.dump(file_data, file_name, indent=4)
