#login testmailasmtp@gmail.com
#hasło testsmtp

import smtplib
import datetime as dt
import random

my_email = "testmailasmtp@gmail.com"
password = "testsmtp"

now = dt.datetime.now()

year = now.year
month = now.month
day_of_week = now.weekday()


quotes = open("quotes.txt", "r")
# print(quotes.readline())
quotes_list = []
for line in quotes:
    quotes_list.append(line)

# random_quote = quotes_list[random.randint(0, len(quotes_list) - 1)]
random_quote = random.choice(quotes_list)

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # enkrypcja maila, zabezpieczenie połączenia
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="przem.pb@gmail.com",
                            msg=f"Subject: Quote of the day! \n\n {random_quote}")

quotes_list.remove(random_quote)

quotes.close()





# if year == 2021:
#     print("gówniana sprwa")

# print(now, year, month, day_of_week)

# date_of_birth = dt.datetime(year=1991, month=10, day=14, hour=4)
#
# print(date_of_birth)