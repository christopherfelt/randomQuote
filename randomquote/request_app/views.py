from django.shortcuts import render

import requests


# Create your views here.


def index(request):
    r = requests.get('https://talaikis.com/api/quotes/random/')
    return_json = r.json()
    author = return_json['author']
    quote = return_json['quote']

    request_dict = {}

    request_dict['author']=author
    request_dict['quote']=quote


    return render(request, 'index.html', context=request_dict)