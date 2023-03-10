import requests
import json
import sys
from twilio.rest import Client
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, r'D:\projects\Udemy\100-days-of-code-Python')
from config_ import *
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

Twilio_sid = ''
Twilio_auth_token=''

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_url = "https://www.alphavantage.co/query"
params = {}
params['function'] = "TIME_SERIES_DAILY_ADJUSTED"
params['symbol'] = STOCK
params['apikey'] = alpha_api_key
#params['interval'] = "60min"

response = requests.get(url=api_url,params=params)
response = response.json()

data = iter(response["Time Series (Daily)"].values())
first_data,second_data = next(data),next(data)


diff = float(first_data['2. high']) - float(second_data['2. high'])
if diff > 0:
    up_down = "U+2B06"
else:
    up_down = "U+2B07"
percentage = round(abs(diff)/float(first_data['2. high'])*100)
if percentage>=5:
    print("Get News")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
new_api = "https://newsapi.org/v2/everything"
params= dict()
params['qinTitle'] = "tesla"
params['from'] = "2023-02-09"
params['sortBy'] = "publishedAt"
params['apiKey'] = news_api_key
params['language'] = 'en'
news_response = requests.get(new_api,params=params)
news_response =news_response.json()
three_article = news_response['articles'][0:3]
#new_response = json.dumps(news_response,indent =4)
#for i in article:
#    print(i)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
article_list = [f"{STOCK}: {up_down}{percentage}% \nHead Lines:{article['title']}. \nBrief: {article['description']}" for article in three_article]


#Optional: Format the SMS message like this: 

client = Client(Twilio_sid,Twilio_auth_token)
for article in article_list:
    message = client.message.create(
        body = article,
        from_ = "",
        to = "",
    )
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

