# import smtplib
# my_email="rub@gmail.com"
#
# password="tfsdzlmmzuecewyb"
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="",msg="Subject:testing python code\n\nusing smtplib to send email with python")
# import datetime as dt
# current_date_time=dt.datetime.now()
# year=current_date_time
# if year==2029:
#     print("__")
# else:
#     print("its 2025")
# print(current_date_time.year)
# print(current_date_time.month)
# print(current_date_time.weekday())
# # 0:monday,1:tuesday,2:wednesday and so on.
# my_date_of_birth=dt.datetime(day=4,month=1,year=2003)
# print(my_date_of_birth.weekday())
# print(my_date_of_birth)
import random
import datetime as dt
import smtplib

current_date=dt.datetime.now()
weeday=current_date.weekday()
if weeday==2:

    with open("quotes.txt") as data:
        quotes_list=data.readlines()
        random_qoute=random.choice(quotes_list)
        print(random_qoute)

        my_email="rub@gmail.com"
        password="vhrllfntnfgexoan"
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)

            connection.sendmail(from_addr=my_email,to_addrs=f"nid_______0404@gmail.com",msg=f"Subject: Quote of the day\n\n{random_qoute}")


