import requests

from twilio.rest import Client

account_sid="AC261816a56dcff008b296f64e0db556dd"
auth_token="bea45fd7f803e9eead7b8ba518da8e19"


stock_api_key="DGA7VHW4VCDJA2YC"
key2= "7LSI5QUB89XRHDF9"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&interval=5min&apikey=key2 "
news_api="b7e0fdd33ae5493ebc133b13fe69c84f"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?q=Tesla Inc&language=en&apiKey=b7e0fdd33ae5493ebc133b13fe69c84f"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response=requests.get(STOCK_ENDPOINT)
data=response.json()["Time Series (Daily)"]
print(data)
new_list=[value for key,value in data.items()]
yesterdays_close_print=new_list[0]["4. close"]
print(yesterdays_close_print)
#
#
# # #TODO 2. - Get the day before yesterday's closing stock price
daybefore_yesterday_closing_print=new_list[1]["4. close"]
print(daybefore_yesterday_closing_print)
# #
# # #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=float(yesterdays_close_print)-float(daybefore_yesterday_closing_print)
print(difference)
up_down=None
if difference<0:
    up_down="📉"
else:
    up_down="📈"
average=(float(yesterdays_close_print)+float(daybefore_yesterday_closing_print))/2
print(average)
# # #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference=round(difference/average)*100
print(percentage_difference)
# #TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_difference)>5:
    print("get news")
    current_news=requests.get(url=NEWS_ENDPOINT)
    data=current_news.json()["articles"][0:3]
    print(data)
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    title_article=[f"{STOCK_NAME}:{up_down}{percentage_difference}\nHeadlines:{items["title"]}\nBreief:{items["description"]}" for items in data]

    for item in title_article:
        print(item)
# description_article=[items["description"] for items in data]
# print(description_article)
# print(description_article[0])
#TODO 9. - Send each article as a separate message via Twilio.
#
        client = Client(account_sid, auth_token)
        message = client.messages.create(

            from_="whatsapp:+14155238886",
            body=item,
            to="whatsapp:+97063"
        )

        print(message.status)

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

