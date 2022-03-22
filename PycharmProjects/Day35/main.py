import requests
import os
from twilio.rest import Client

params={
    "lat":36.561325,
    "lon":136.656204,
    "exclude":"current,minutely,daily",
    "appid":"f6bdd65d8c8451914e478a4c8c232016"
}
from twilio.http.http_client import TwilioHttpClient
proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})


response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=params)
response.raise_for_status()
weather_data = response.json()
slice_weather=weather_data["hourly"][:12]
prec=[hour["weather"][0]["id"] for hour in slice_weather]
willrain=False
for i in prec:
    if int(i)<800:
        print("Bring an umbrella")
        willrain=True
        break
if willrain:
    account_sid = "ACfcc124b5963a67c4d505ba4b2a5183d4"
    auth_token = "5f781a597e9c3ef597c75ce7c79dd646"

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                         body="Bring an ☂️",
                         from_='+19383003849',
                         to='+919819763821'
                     )

    print(message)

# import requests
# import os
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
#
# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = os.environ.get("OWM_API_KEY")
# account_sid = "YOUR ACCOUNT SID"
# auth_token = os.environ.get("AUTH_TOKEN")
#
# weather_params = {
#     "lat": "19.076090",
#     "lon": "72.877426",
#     "appid": "f6bdd65d8c8451914e478a4c8c232016",
#     "exclude": "current,minutely,daily"
# }
#
# response = requests.get(OWM_Endpoint, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]
#
# will_rain = False
#
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#
#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages \
#         .create(
#         body="It's going to rain today. Remember to bring an ☔️",
#         from_="+19383003849",
#         to="+919819763821"
#     )
#     print(message.status)