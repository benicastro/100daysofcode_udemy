"""
Workout Tracker via Google Sheets by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules/libraries ###
import requests
from datetime import datetime as dt

# Create constant/global variables
APP_ID = "4c8b271c"
APP_KEY = "fb0f6829fe041688c86838d0b427ffde"

AGE = 29
GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 172

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = (
    "https://api.sheety.co/17d8fefb19eab46bd53463191a3510a8/workoutTracking/workouts"
)

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
    "Authorization": "Basic bnVsbDpudWxs",
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

print(sheet_response.text)
