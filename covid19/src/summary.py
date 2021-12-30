# from covid19.src.apis import covid19api
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

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
job = None

def tick():
    print('One tick!')

def start_job():
    global job
    job = scheduler.add_job(tick, 'interval', seconds=5)
    try:
        scheduler.start()
    except:
        pass

start_job()