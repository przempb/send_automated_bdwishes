##################### Automation b-day wishes ######################

import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "testmailasmtp@gmail.com"
password = "yfuttzrpzuhircwx"


now = dt.datetime.now()
month = now.month
day_of_week = now.day
year = now.year
hour = now.hour

birthday_csv = pd.read_csv("birthdays.csv")

df = pd.DataFrame(data=birthday_csv, columns=["name", "email", "year", "month", "day"])

solenizant = df.loc[(df["month"] == month) & (df["day"] == day_of_week)]
solenizant_name = solenizant["name"].item()
solenizant_month = solenizant["month"].item()
solenizant_day = solenizant["day"].item()

birthday_day = birthday_csv["day"]
birthday_month = birthday_csv["month"]


if month == solenizant_month and day_of_week == solenizant_day:
    template = f'letter_{random.randint(1, 3)}.txt'
    messagein = open(f"C:/Users/przem/PycharmProjects/automatedbdwishes/letter_templates/{template}", "rt")
    messageout = open(f"C:/Users/przem/PycharmProjects/automatedbdwishes/letter_templates/sent to {solenizant_name} in {year}, {hour}.txt", "w+")

    for line in messagein:
        messageout.write(line.replace("[NAME]", solenizant_name))

    messageout.close()
    messagein.close()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        with open(f"C:/Users/przem/PycharmProjects/automatedbdwishes/letter_templates/sent to {solenizant_name} in {year}, {hour}.txt", "rt") as to_send:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="przem.pb@gmail.com",
                                    msg=f"Subject:Wszystkiego najlepszego, {solenizant_name}! \n\n {to_send.read()}")
                print(to_send.read())

