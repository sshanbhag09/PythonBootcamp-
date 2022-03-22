# import datetime as dt
# import smtplib
# my_email="appbreweryinfosushant@gmail.com"
# password="RGSS0103sus@"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="appbrewerrtestingsus@yahoo.com",msg="Subject:hi message\n\nHello")
# now = dt.datetime.now()
#
# date_of_birth=dt.datetime(year=1999,month=10,day=28)
# print(date_of_birth)

import smtplib
import random
import datetime as dt

now = dt.datetime.now()
day=now.weekday()
if day==1:
    with open("quotes.txt","r") as quotes:
        line=quotes.read().splitlines()
        selected_quote=random.choice(line)
        print(selected_quote)
        my_email="appbreweryinfosushant@gmail.com"
        password="RGSS0103sus@"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs="appbrewerrtestingsus@yahoo.com",msg=f"Subject:quote message\n\n{selected_quote}")
