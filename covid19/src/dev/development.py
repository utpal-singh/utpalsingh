from covid19.src.dev.api_time import url

import requests

apiHandler = url

rawData = requests.get(apiHandler)

dict_results = rawData.json()

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
job = None

def get_raw_data():
    rawData = requests.get(apiHandler)

    dict_results = rawData.json()
    return dict_results

def start_job():
    global job
    job = scheduler.add_job(get_raw_data, 'interval', seconds=60)
    try:
        scheduler.start()
    except:
        pass

# start_job()

