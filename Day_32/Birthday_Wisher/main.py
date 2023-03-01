import smtplib
import random
import datetime as dt

# ------------------------- Reading quotes ---------------------- #
def sending_quotes():
    with open("quotes.txt")as f:
        quotes = f.read()
    quotes = quotes.split('\n')
    msg = random.choice(quotes)
    my_email = "demo@gmail.com"
    password = ""
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="demo2@gmail.com",
                            msg=f"Subject:Morning Quotes\n\n{msg}")


now = dt.datetime.now()
print(now.weekday())
if now.weekday() == 1:
    sending_quotes()
#
#
#now =dt.datetime.now()
#year = now.year
#month = now.month
#day = now.day
#day_of_week = now.weekday()
#print(day_of_week)
#
#date_of_birth = dt.datetime(year=1998,month=4,day=13)
#print(date_of_birth)




