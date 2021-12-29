from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from covid19.src import summary

# import requests

# from covid19.apis import covid19api

def index(request):
    #results = requests.get(covid19api+"/summary")
    # return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "results": results.json()})
    return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "date" : summary.date, "datedayyr" : summary.datedayyr, "timeh" : summary.timeh, "timem" : summary.timem, "times" : summary.times, 'globalstats' : summary.global_stats})