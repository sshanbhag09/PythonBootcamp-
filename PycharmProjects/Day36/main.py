STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API="1f5492b3eba442e8bc2fb71d330c17ad"
STOCK_API="YH7LPRZ0IQBZOB77"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import requests
from twilio.rest import Client
from newsapi import NewsApiClient


stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":"YH7LPRZ0IQBZOB77"
}
response = requests.get(url=STOCK_ENDPOINT,params=stock_params)

data = response.json()


slice_Data=data["Time Series (Daily)"]
list = [(k,v) for k, v in slice_Data.items()][:2]


todaydate=list[0][0]
yestdate=list[1][0]

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
i=0
today=float(list[i][1]['4. close'])
yest=float(list[i+1][1]["4. close"])
perc=(today-yest)/today *100
if perc>0 and perc>=5:
    news_params={
        "qInTitle":COMPANY_NAME,
        "apikey":NEWS_API
    }
    response_news = requests.get(url=NEWS_ENDPOINT,params=news_params)

    news_data = response_news.json()
    list_articles=news_data["articles"]
    artic=[item for item in list_articles][:3]
    for item in artic:
        print(item)
# elif perc<0 and abs(perc)>5:
#     print("Get News Neg")



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator





## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.
account_sid = "ACfcc124b5963a67c4d505ba4b2a5183d4"
auth_token = "5f781a597e9c3ef597c75ce7c79dd646"


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
