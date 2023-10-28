import datetime
from datetime import datetime
import requests


NUTRI_API_APP_ID = "0df0c43f"
NUTRI_API_APP_KEY = "2cdb8b94ba0edc469fb445b011c7b0c6"
SHEETY_API_KEY= "Basic YmV6YzoxMjM0NTY3OA=="

nutri_entrypoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_entrypoint = "https://api.sheety.co/296db57bc276f3662fd279cc0d211792/workoutTracker/workouts"


def ask_nutri():
    nutri_headers = {
        "x-app-id": NUTRI_API_APP_ID,
        "x-app-key": NUTRI_API_APP_KEY
    }

    nutri_query = {
        "query": input("What did you do today?")
    }

    response = requests.post(url=nutri_entrypoint, json=nutri_query, headers=nutri_headers)
    print(response.json())
    return response.json()['exercises']


def update_sheet(content):

    now = datetime.today()

    sheety_headers = {
        "Authorization": SHEETY_API_KEY
    }

    for entry in content:

        sheety_post = {
            "workout":
                {
                "date": f"{now.strftime('%d/%m/%Y')}",
                "time": f"{now.strftime('%H:%M:%S')}",
                "exercise": f"{entry['name']}",
                "duration": f"{entry['duration_min']}",
                "calories": f"{entry['nf_calories']}"
                }
        }

        response = requests.post(url=sheety_entrypoint, json=sheety_post, headers=sheety_headers, verify=False)
        print(response.json())


update_sheet(ask_nutri())