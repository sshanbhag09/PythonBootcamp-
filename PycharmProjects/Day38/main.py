import requests
import datetime
GENDER = 'male'
WEIGHT_KG = 68
HEIGHT_CM = 176
AGE = 21

API_KEY = '75c17366ba51ee0ebd7642404ab9079d'
APP_ID = 'c41bce58'

API_SHEETY='26b34674d78451aaafb6f0ef6076b5fe'
projectName_sheety='copyOfMyWorkouts'
SHEET_NAME='workouts'
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint='https://api.sheety.co'
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
header_sheety={
    'username':API_SHEETY,
    'projectName':projectName_sheety,
    'sheetName':SHEET_NAME
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

print(result)
# parameter_sheety={
#     'Date':datetime.date,
#     'Time':datetime.time,
#     'Exercise':result['exercises']['name'],
#     'Duration':result['exercise']['duration_min'],
#     'Calories':result['exercise']['nf_calories']
# }

# respexc=requests.post(sheety_endpoint,json=parameter_sheety,headers=header_sheety);
#res_list=[value for key,value in result.items]
print(result['exercises'])
print()
print(datetime.time())