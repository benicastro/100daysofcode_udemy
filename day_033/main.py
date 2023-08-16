"""
ISS Overhead Notifier Project by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules ################################################################################################################
import datetime as dt
import requests
import smtplib
import time

# Declare constant Variables ###########################################################################################################
MY_EMAIL = "pythonuniversality@gmail.com"
PASSWORD = "toldvfdeodjzypbo"
ISS_API = "http://api.open-notify.org/iss-now.json"
SUNS_API = "https://api.sunrise-sunset.org/json"
MY_LAT = 15.505904
MY_LON = 480.986609


# Main #################################################################################################################################

# Create functions
def is_close():
    """This functions takes in the current ISS position and returns true if it is within +-5 degrees to my position."""
    # Get ISS coordinates
    iss_response = requests.get(ISS_API)
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_position = (float(iss_data["iss_position"]["latitude"]), float(iss_data["iss_position"]["longitude"]))
    return (iss_position[0] - 5 <= MY_LAT <= iss_position[0] + 5) and (iss_position[1] - 5 <= MY_LON <= iss_position[1] + 5)


def is_time():
    """This functions returns true if it is possible to see the ISS at the given times."""
    # Create a dictionary for the parameters of the sunset-sunrise API
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "formatted": 0,
    }
    # Get the current time (hour)
    current_time = dt.datetime.now().hour
    # Get sunset and sunrise times for current date
    suns_response = requests.get(SUNS_API, params=parameters)
    suns_response.raise_for_status()
    suns_data = suns_response.json()
    sunrise_time = int(suns_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_time = int(suns_data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunset_time > current_time or current_time < sunrise_time


# Send email message as notification if ISS is near me
while True:
    time.sleep(60)
    if is_close() and is_time():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="benedict.zcastro@gmail.com",
                msg="Subject: ISS Notification \n\nLook up! The ISS is above you in the sky.",
            )
