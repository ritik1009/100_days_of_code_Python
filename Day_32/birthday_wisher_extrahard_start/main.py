##################### Extra Hard Starting Project ######################
import pandas as pd
from datetime import datetime
import random
import smtplib

now = datetime.now()


def sending_mail(letter='',to = ''):
    my_email = "demo@gmail.com"
    password = ""
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to,
                            msg=f"Subject:Happy Birthday\n\n{letter}")



# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")
#-------------------- Adding data in df -------------------#
birthdates = {
    "name":["Ritik","Chintu"],
    "email":["khandelw@gmail.com","chirag@gmail.com"],
    "year":[1999,2005],
    "month":[3,2],
    "day":[1,28]}
df2 = pd.DataFrame(birthdates)
df = pd.concat([df[0:1], df2], ignore_index=True)

# 2. Check if today matches a birthday in the birthdays.csv
wish = df[(df.month == now.month) & (df.day == now.day)]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#print(type(wish))
if len(wish) > 0:
    for i in wish.index:
        choose = random.randint(1,3)
        with open(f"letter_templates\letter_{str(choose)}.txt")as f:
            letter = f.read()
        name = wish['name'][i]
        email = wish['email'][i]
        letter = letter.replace("[NAME]",name)
        print("\n email",email)
        sending_mail(letter=letter,to=email)
        #print(letter)

#4. Send the letter generated in step 3 to that person's email address.






