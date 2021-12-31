# from covid19.src.apis import covid19api
from covid19.src.apis import covid19api
import requests
import datetime
import dateutil.parser
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
job = None
# import time

# apiHandler = covid19api + "/summary"
apiHandler = covid19api + "/summary"

# rawData = requests.get(apiHandler)

# dict_results = rawData.json()

# date = dict_results['Date']

# d = dateutil.parser.parse(date)
# datedayyr = d.strftime('%m/%d/%Y')
# timeh = d.strftime('%H')
# timem = d.strftime('%M')
# times = d.strftime('%S')



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


# while True:
#     global_stats = dict_results['Global']
#     print(global_stats)
#     time.sleep(10)

# import subprocess
# import threading
# import time


# def ping():
#     while True:
#         print("Pinging ...") # do actual API pinging stuff here
#         time.sleep(10)

# t = threading.Thread(target=ping)
# t.start() # this will run the `ping` function in a separate thread

# from apscheduler.schedulers.background import BackgroundScheduler



# def tick():
#     print('One tick!')

def start_job():
    global job
    job = scheduler.add_job(get_data, 'interval', seconds=3600)
    try:
        scheduler.start()
    except:
        pass

start_job()