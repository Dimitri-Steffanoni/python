import schedule
import time
import requests
from twilio.rest import Client
from datetime import datetime

def sms():
    print("Start")

    api_key = "049f327d8a59ac1a2f08a7d75ec396ba"
    OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"

    account_sid = 'ACc7855a5c8bfff9d9a0a164ea10740e15'
    auth_token = 'b122d189087462200a49a2358beeb9df'

    param = {
        "lat": 45.4642,
        "lon": 9.1900,
        "appid": api_key
    }

    response = requests.get(OWM_Endpoint, params=param)
    response.raise_for_status()

    weather_data = response.json()
    weather_slice = weather_data["list"][:5]


    will_rain = False

    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
          will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain in Milan today. Remember to bring an ☂️",
            from_='+19789193325',
            to='+393453398508'
        )
        print("Sent SMS")


    print("End")

def job():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    sms()
#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("07:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(30)