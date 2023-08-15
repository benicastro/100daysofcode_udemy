"""
Automatic Birthday Wisher Project by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
import pandas as pd
import datetime as dt
import smtplib
import random

# Declare constant variables
MY_EMAIL = "pythonuniversality@gmail.com"
PASSWORD = "toldvfdeodjzypbo"

# Create a tuple for today's date
today = (dt.datetime.now().month, dt.datetime.now().day)

# Read the csv file and save to a dictionary
birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays.iterrows()}

# Check if today's date is in the birthdays dictionary and sent to the person celebrating
if today in birthdays_dict:
    with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter_content = letter_file.read()
        letter_message = letter_content.replace("[NAME]", birthdays_dict[today]["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthdays_dict[today]["email"],
                            msg=f"Subject: Happy Birthday\n\n{letter_message}",
                            )
