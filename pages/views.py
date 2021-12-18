from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "pages/index.html", {"title": "Home - Utpal Singh"})


# Create your views here.
