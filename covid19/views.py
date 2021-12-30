from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from covid19.src import summary


# import requests

# from covid19.apis import covid19api

def index(request):
    #results = requests.get(covid19api+"/summary")
    # return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "results": results.json()})
    # while True:
    #     print(summary.timeh)
    # return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "date" : summary.date, "datedayyr" : summary.datedayyr, "timeh" : summary.timeh, "timem" : summary.timem, "times" : summary.times, 'globalstats' : summary.global_stats})

    while True:
        from covid19.src.apis import covid19api
        import requests
        import datetime
        import dateutil.parser
        # import time

        # apiHandler = covid19api + "/summary"
        apiHandler = covid19api + "/summary"

        rawData = requests.get(apiHandler)

        dict_results = rawData.json()

        date = dict_results['Date']

        d = dateutil.parser.parse(date)
        datedayyr = d.strftime('%m/%d/%Y')
        timeh = d.strftime('%H')
        timem = d.strftime('%M')
        times = d.strftime('%S')

        global_stats = dict_results['Global']
        return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "date" : date, "datedayyr" : datedayyr, "timeh" : timeh, "timem" : timem, "times" : times, 'globalstats' : global_stats})

