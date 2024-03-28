from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')

nutritionix_stem = 'https://trackapi.nutritionix.com'
nlp_exercise_endpoint = '/v2/natural/exercise'
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
params = {
    'query': input('What exercise did you do? ')
}

response = requests.post(url=nutritionix_stem+nlp_exercise_endpoint, json=params, headers=headers)
response.raise_for_status()
data = response.json()

sheety_stem = 'https://api.sheety.co'
sheety_endpoint = '/d9f02081f9a01191e5a5c45c80a67854/myWorkouts (pythonProject)/workouts'
headers = {
    'Authorization': SHEETY_TOKEN,
    'Content-Type': 'application/json'
}
for exercise in data['exercises']:
    row = {
        'workout': {
            'date': datetime.now().strftime('%d/%m/%Y'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    response = requests.post(url=sheety_stem+sheety_endpoint, json=row, headers=headers)
    response.raise_for_status()