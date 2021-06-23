from django.shortcuts import render
import requests
from datetime import date
import json
import time


API_KEY = '91bbdf9adfeb4c0f8e046fb4e1e58933'
DATE = date.today()

# Create your views here.

def home(request):
    url = f'https://newsapi.org/v2/everything?q=gaming&from={DATE}&sortBy=popularity&language=en&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']
    
    context ={
	    'articles' : articles
    }

    return render(request, 'news/home.html', context)

def archive(request):
    url = f'https://newsapi.org/v2/everything?q=gaming&from={DATE}&sortBy=popularity&language=en&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    
    with open('data.json', 'r') as fp:
        obj = json.load(fp)

    articles = obj['articles']

    context={
        'articles' : articles
    }


    return render(request, 'news/archive.html', context)

    
def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        url1 = f'https://newsapi.org/v2/everything?q=gaming+q={query}&sortBy=popularity&language=en&apiKey={API_KEY}'
        response = requests.get(url1)
        data = response.json()

        articles= data['articles']

        context={
            'articles' : articles
        }    

        return render(request, 'news/search.html', context)



