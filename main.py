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
    'query': 'Ran for 2 miles'
}

response = requests.post(url=nutritionix_stem+nlp_exercise_endpoint, json=params, headers=headers)
response.raise_for_status()
data = response.json()