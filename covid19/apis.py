covid19tracker_hist_data = "https://api.covid19tracker.in/data/static/timeseries.min.json"
covid19tracker_current_day = "https://api.covid19tracker.in/data/static/data.min.json"



from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

def FirstCronTest():
    covid19api = "https://api.covid19api.com"
    print("")
    print("I am executed..!")
    return covid19api


scheduler.add_job(FirstCronTest, 'interval', seconds=10)
scheduler.start()