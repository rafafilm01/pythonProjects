#send motivational quoates on each Monday 
from email import message
import random
import smtplib
import datetime as dt

my_email= 'szymaniuk1983@gmail.com'
my_password = 'passgen02' #PASSWORD NEEDS UPDATING TO THE ACTUAL ONE


#open qutes.txt to get a list of quotes
with open('quotes.txt') as file:
    quotes =file.readlines()    #converts the sting into a list
    random_quote = random.choice(quotes)
    # print(random_quote) #SANITY CHECK
    
#obtain current day of the week
    current_date = dt.datetime.now()
    current_day_of_the_week =current_date.weekday()
    # print(current_day_of_the_week) # SANITY CHECK 

    #check to see if the current day is a Monday  in order to carry out the rest of the code 
    #EDIT VALUE TO STOP / START SEDNING TEST EMAILS 0 = Monday, 1=Tuesday etc
    if current_day_of_the_week ==2:
        # print('today is a Monday, here is your motivation !  ') #SANITY CHECK
        
        
    #use smtplib to send the random email
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='rafafilm01@hotmail.com',
                msg=f'Subject: motivation for Monday \n\n {random_quote} '
                
                
            )
    else:
        print('sorry it is not Monday. No motivation for you ')




#user random module to pick  a quote for the day


