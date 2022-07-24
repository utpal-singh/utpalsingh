import requests
import datetime
import dateutil.parser

apiHandler = "https://api.crossref.org/works/" + doi



def get_data():
    rawData = requests.get(apiHandler)

    dict_results = rawData.json()
    global_stats = dict_results['Global']

    date = dict_results['Date']

    d = dateutil.parser.parse(date)
    datedayyr = d.strftime('%m/%d/%Y')
    timeh = d.strftime('%H')
    timem = d.strftime('%M')
    times = d.strftime('%S')
    return datedayyr, timeh, timem, times, date, global_stats
