from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request, "pages/index.html", {"title": "Home - Utpal Singh"})

def about(request):
    return render(request, "pages/about.html", {"title": "About - Utpal Singh"})

def contact(request):
    return render(request, "pages/contact.html", {"title": "Contact - Utpal Singh"})
    
def google_verification(request):
    return render(request, "pages/googlea3fa796d88ba8a2b.html")

def cite(request):
    if request.method == 'POST':
        doi_url= request.POST["doi"]
        if doi_url[:5] == "https":
            doi_url = doi_url[16:]
        if doi_url[:8] == "doi.org/":
            doi_url = doi_url[8:]
        apiHandler = "https://api.crossref.org/works/" + doi_url
        rawdata = requests.get(apiHandler)
        dict_results = rawdata.json()
        apa7th = dict_results["message"]["author"][0]["family"] + " " + \
        dict_results["message"]["author"][0]["family"][:1] + ". " + \
        str(dict_results["message"]["issued"]["date-parts"][0][0]) + ", " + \
        dict_results["message"]["title"][0] + ", " + \
        dict_results["message"]["container-title"][0] + ", " + \
        dict_results["message"]["volume"] + dict_results["message"]["DOI"]
   
        dict = {
           'doi_url': apa7th
      }
    return render(request, 'cite.html', dict)   



# Create your views here.
