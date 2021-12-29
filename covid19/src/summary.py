from covid19.src.apis import covid19api
import requests
import datetime
import dateutil.parser

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