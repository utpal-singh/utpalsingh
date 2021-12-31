from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from covid19.src import summary

from covid19.src.dev.development import results


# import requests

# from covid19.apis import covid19api

def index(request):
    #results = requests.get(covid19api+"/summary")
    # return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "results": results.json()})
    # while True:
    #     print(summary.timeh)
    return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "date" : summary.get_data()[4], "datedayyr" : summary.get_data()[0], "timeh" : summary.get_data()[1], "timem" : summary.get_data()[2], "times" : summary.get_data()[3], 'globalstats' : summary.get_data()[5]})

    # while True:
        # from covid19.src.apis import covid19api
        # import requests
        # import datetime
        # import dateutil.parser
        # # import time

        # # apiHandler = covid19api + "/summary"
        # apiHandler = covid19api + "/summary"

        # rawData = requests.get(apiHandler)

        # dict_results = rawData.json()

        # date = dict_results['Date']

        # d = dateutil.parser.parse(date)
        # datedayyr = d.strftime('%m/%d/%Y')
        # timeh = d.strftime('%H')
        # timem = d.strftime('%M')
        # times = d.strftime('%S')

        # global_stats = dict_results['Global']
        # return render(request, "covid19/index.html", {"title": "Home - Utpal Singh", "date" : date, "datedayyr" : datedayyr, "timeh" : timeh, "timem" : timem, "times" : times, 'globalstats' : global_stats})

def development(request):
    # import requests
    # apiHandler = "http://worldtimeapi.org/api/timezone/Asia/Kolkata"
    # rawData = requests.get(apiHandler)
    # dict_result = rawData.json()
    return render(request, "covid19/development.html", {"variable" : results})