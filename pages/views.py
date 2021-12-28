from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "pages/index.html", {"title": "Home - Utpal Singh"})

def about(request):
    return render(request, "pages/about.html", {"title": "About - Utpal Singh"})

def contact(request):
    return render(request, "pages/contact.html", {"title": "Contact - Utpal Singh"})
    
def google_verification(request):
    return render(request, "pages/googlea3fa796d88ba8a2b.html")





# Create your views here.
