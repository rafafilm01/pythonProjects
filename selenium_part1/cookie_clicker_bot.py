# objective - create cookie clicker bot that automatically plays the game and racks up a high score in 5 minutes , compare the score and find the most efficient way to play the game 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service('C:\development\chromedriver.exe')
URL = 'http://orteil.dashnet.org/experiments/cookie/'

driver = webdriver.Chrome(service=service)

driver.get(URL)

#find the cookie to click on 
def click_cookie():
    cookie = driver.find_element(By.ID,'cookie')
    cookie.click()
    #changing the values in the timer will decrease the lenght of loops and therefore speed up the number of clicks per second
    time.sleep(0.0001)


#create a time loop for 5 minutes 
import time
timeout = time.time() + 60*5   # 5 minutes from now
#seconds_timer as tool to carry on counting loops and once a specific number of clicks have been reached , carry out an acttivity (purchase more items)
seconds_timer =0
while True:
    
    test = 0
    click_cookie()
    seconds_timer +=1
    print(seconds_timer)
    
    cookie_counter = driver.find_element(By.ID,'money')
    if seconds_timer >50:
        print("shopping time... ")
        
    
        factory = driver.find_element(By.XPATH,'//*[@id="buyFactory"]')
        factory.click()
        print('factory starting up...')
        time.sleep(0.1)
    
        grandma = driver.find_element(By.XPATH,'//*[@id="buyGrandma"]')
        grandma.click()
        print('grandma on the way...')
        time.sleep(0.1)
    
        cursor_button =driver.find_element(By.XPATH,'//*[@id="buyCursor"]')
        cursor_button.click()
        print('another cursos deployed...')
        time.sleep(0.1)
        
        seconds_timer =0
    if test == 5 or time.time() > timeout:
        break
    test = test - 1


#check the final cookie count and ratio
cookie_counter = driver.find_element(By.ID,'money')
print(f'total cookie count is : {cookie_counter.text}')
cps = driver.find_element(By.ID,'cps')
print(f'your cookie per second ratio is: {cps.text}')
    
    
#leave the web page running 
#driver.close()