##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import  pandas as pd
import smtplib
import datetime as dt
import os,random
birth_read=pd.read_csv("birthdays.csv")
birth_dict={}
for(index,row) in birth_read.iterrows():
    birth_dict[(row.month,row.day)]=row
print(birth_dict)
today_date=dt.datetime.now()

if (today_date.month,today_date.day) in birth_dict:
    selected_letter=random.choice(os.listdir("letter_templates"))
    selc=random.randint(1,3)
    birth_df=birth_dict[(today_date.month,today_date.day)]
    name=birth_df['name']
    email1=birth_df['email']
    print(email1)
    with open(f"letter_templates/letter_{selc}.txt") as file:
        content=file.read()


        content=content.replace("[NAME]",name)
        print(content)
        my_email="appbreweryinfosushant@gmail.com"
        password="RGSS0103sus@"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=email1,msg=f"Subject:Birthday message\n\n{content}")




