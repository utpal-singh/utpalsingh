from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import requests

from covid19.apis import covid19api

def index(request):
    results = requests.get(covid19api+"/summary")
    return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "results": results.json()})