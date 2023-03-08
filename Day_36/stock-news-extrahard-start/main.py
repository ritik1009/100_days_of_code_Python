import requests
import json
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_api_key = '19UX710W1AYV23IR'
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






#response_yesterday = response['Time Series (Daily)']['']

#response = json.dumps(response,indent=4)
#print(response)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

