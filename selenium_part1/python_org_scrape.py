#objective , scrape the web callendar for events from python.org. and save into a dictionary format

#import webdriver from selenium
from selenium import webdriver

#additional libs needed to access the data from a webpage (2022)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service needs to be pointing to chromedriver module on the disk (or any other driver that will be used )
service = Service('C:\development\chromedriver.exe')

URL ='https://www.python.org/'
dates_list =[]
event_list =[]


driver = webdriver.Chrome(service=service)
driver.get(URL)

#access names of links and dates of events seperately using xpath, each item found gets added to their own dedicated lists

#locate dates
#while loop designed to increment xpath item by 1 in order to iterate over the changed  path and retrieve extra data , i < condition  can match the number of rows in the calendar on python.org or can be larger , in this case selenium is not finding any matches and it does not crash the prog. 
i=1
while i<8:
    
    event_dates = driver.find_elements(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
#for loop designed to iterate over and capture each entry from the calendar for dates
    for item in event_dates:
        text =item.text
        dates_list.append(text)
        # print(text) #SANITY CHECK
        
    #locate event links
    event_links = driver.find_elements(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
#for loop designed to iterate over and capture each entry from the calendar for events
    for item in event_links:
        text =item.text
        event_list.append(text)
        # print(text) #SANITY CHECK 
        
# at the end of 1st for loop increase the variable nad go through the loop again . All the way to specified while condition is fullfiled 
    i =i+1
    
    
# print(dates_list) #SANITY CHECK
# print(event_list) #SANITY CHECK


# create a dict using 2 lists with zip() and dict() functions. Zip() matches the 2 lists together item by item. Further conversion by dict() is to create a readbale usable dictionary object from the zip element 
events =zip(dates_list, event_list)
events_dict= dict(events)
print(events_dict)


# NOTE !! textbook example : 
#using a unique class name to access the correct table , use  multiple selectors at the time by putting a (space) in between them 


dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
 
events_dict = {}

#for loop to build the dictionary 
for i in range(len(events)-1):
    full_date = dates[i].get_attribute("datetime").split("T")[0]
    # gets the full date with year (the solution from the Course gives only the date without year)
    
    events_dict[i]= {
        'time': full_date,
        'name': events[i].text
        }

print('-------------') 
print(events_dict)


driver.close()