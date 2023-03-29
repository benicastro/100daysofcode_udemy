"""
Stock Trading News Alert Project by: Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules/libraries ######################################################################################################
import requests
import smtplib
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

# Declare constant variables ###########################################################################################################
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_STOCK_KEY = os.environ.get("API_STOCK_KEY")
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_STOCK_KEY,
}

API_NEWS_KEY = os.environ.get("API_NEWS_KEY")
NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": API_NEWS_KEY,
}

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

# Main #################################################################################################################################

# Fetch stock data and convert to list
stocks_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()["Time Series (Daily)"]
stocks_data_list = [value for (key, value) in stocks_data.items()]

# Extract the stocks data for specific dates and calculate the percentage difference
stocks_yesterday_close = float(stocks_data_list[0]["4. close"])
stocks_yesterday2_close = float(stocks_data_list[1]["4. close"])

difference = stocks_yesterday_close - stocks_yesterday2_close

if difference <= 0:
    change = f"The stock price went down by {difference}$."
else:
    change = f"The stock price went up by {difference}$."

# Get the first articles related to the company if the percentage difference is greater than 1
percent_difference = (abs(difference)/stocks_yesterday_close) * 100
if percent_difference > 1:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    articles = news_response.json()["articles"]
    top_articles = articles[:3]
    articles_content = [f"Headline: {article['title']}. \nBrief Description: {article['description']}" for article in top_articles]

    # Send message to phone and email about the stocks news
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        for article in articles_content:
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="benedict.zcastro@gmail.com",
                                msg=f"Subject: {change}\n\n{str(article.encode('ascii', 'ignore').decode('ascii'))}")
            proxy_client = TwilioHttpClient()
            proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages.create(
                body=f"Subject: {change}\n\n{str(article.encode('ascii', 'ignore').decode('ascii'))}",
                from_=PHONE_NUMBER,
                to=PHONE_NUMBER,
            )

print(message.status)
