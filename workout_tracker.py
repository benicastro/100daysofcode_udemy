"""
Workout Tracker via Google Sheets by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules/libraries ###
import requests
from datetime import datetime as dt
import os

# Create constant/global/environment variables
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

AGE = os.environ["YOUR_AGE"]
GENDER = os.environ["YOUR_GENDER"]
WEIGHT_KG = os.environ["YOUR_WEIGHT"]
HEIGHT_CM = os.environ["YOUR_HEIGHT"]

EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
SHEET_AUTHORIZATION = os.environ["SHEET_AUTHORIZATION"]

# Main Program ###

exercise_query = input("What exercise did you perform?: ")

headers_nutritionix = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(
    EXERCISE_ENDPOINT, json=parameters, headers=headers_nutritionix
)
result = response.json()

# Sheety

headers_sheety = {
    "Authorization": SHEET_AUTHORIZATION,
}

date_now = dt.now().strftime("%d/%m/%Y")
time_now = dt.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheet_response = requests.post(
    SHEET_ENDPOINT, json=sheet_inputs, headers=headers_sheety
)
