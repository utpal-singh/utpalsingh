from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import requests

from covid19.apis import current_day, hist_data

def index(request):
    results = requests.get(current_day)
    return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "results": results.json()})