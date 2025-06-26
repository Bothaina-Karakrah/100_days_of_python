from datetime import datetime
import requests
GENDER = "<YOUR GENDER>"
WEIGHT_KG = "<YOUR WEIGHT KG>"
HEIGHT_CM = "<YOUR HEIGHT CM>"
AGE = "<YOUR AGE>"
APP_ID = "<APP_ID>"
API_KEY = "<API_KEY>"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today = datetime.now()
sheet_endpoint = "https://api.sheety.co/3a18aedeac14a857ee661091b8a50b57/myWorkouts/workouts"
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "Date": today.strftime("%d/%m/%Y"),
            "Time": today.strftime("%H:%M:%S"),
            "Exercise": exercise['user_input'].title(),
            "Duration": exercise['duration_min'],
            "Calories": exercise['nf_calories']
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)