import schedule
import time
from datetime import datetime


def job():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("16:25").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)