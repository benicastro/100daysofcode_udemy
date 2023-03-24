"""
Rain Alert App by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules/libraries ######################################################################################################
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Declare constant variables ###########################################################################################################
MY_LAT = "Latitude"
MY_LON = "Longitude"
API_KEY = os.environ.get("API_KEY")
API_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
ACCOUNT_SID = "AC8b296800c59495d85847c04862ec0ebc"
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
PHONE_NUMBER = "+Phone Number"

PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

# App Main #############################################################################################################################

# Perform an API request
response = requests.get(url=API_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

# Check if there is a chance of rain for the next 12 hours from 07:00
will_rain = False
for i in range(0, 12):
    hourly_weather_id = weather_data["hourly"][i]["weather"][0]["id"]
    if int(hourly_weather_id) < 700:
        will_rain = True
        break

# Set up Twilio and send message if it will rain
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It may rain today, please bring your umbrella.",
        from_=PHONE_NUMBER,
        to=PHONE_NUMBER,
    )

print(message.status)
