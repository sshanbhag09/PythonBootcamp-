import requests
LONG=72.855845
LAT=19.185759
# from requests import Response

response=requests.get("http://api.open-notify.org/iss-now.json")
if response.status_code==404:
    print("page does not exists")
elif response.status_code==401:
    print("you are not authorized to view page")
response.raise_for_status()
data=response.json()
print(data)
longitude=data['iss_position']['longitude']
latitude=data['iss_position']['latitude']
print((longitude,latitude))

# parameters={
#     "lat":LAT,
#     "lng":LONG,
#     "formatted":0
#
# }
# response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
# response.raise_for_status()
# data=response.json()
# sunrise=data['results']['sunrise']
# sunset=data['results']['sunset']
# print(sunrise.split("T"),sunset)