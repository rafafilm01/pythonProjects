# import smtplib

# my_email= 'szymaniuk1983@gmail.com'
# my_password = 'YOUR_PASSWORD_GOES_HERE'

# #example of a test email sent via py, SMTP filed varies depending on email provider, also make sure 2 stap authentication is disabled and access to lesssecure apps is turned on 
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password )
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs='rafafilm01@hotmail.com',
#         msg="Subject: this is a nice heading \n\ngood morning ! This is an example of a test email ")

import datetime as dt
#once we capture currenttime we an start pushing it to dedicated time methods and using them , now() in itslef is messy as it has a lot of data to work with 
# now =dt.datetime.now()
# day =now.day
# minute = now.minute
# hour =now.hour
# print(now)
# print(day)
# current_time =(f'{hour}:{minute}')
# print(current_time)

#setting up a specfic date 
# date_of_birth = dt.datetime(year=1983, month=10, day=12) #the rest of the time detiasl is compulsory
# print(date_of_birth)