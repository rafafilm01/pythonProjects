#objective - sign up for a newsletter on below URL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('C:\development\chromedriver.exe')
URL = 'http://secure-retreat-92358.herokuapp.com/'

driver =webdriver.Chrome(service=service)

driver.get(URL)

#depricated commands 
# name_field = driver.find_element_by_name('fName')
# name_field.send_keys('rafal')


# surname_field =driver.find_element_by_name('lName')
# surname_field.send_keys('szymaniuk')

# email_field = driver.find_element_by_name('email')
# email_field.send_keys('rafafilm01@hotmail.com')

# sign_up_button =driver.find_element_by_link_text('Sign up')
# sign_up_button.send_keys(Keys.ENTER)


#accessing the entry fileds using By. method
name =driver.find_element(By.NAME,'fName')
name.send_keys('rafal2')

surname = driver.find_element(By.NAME,'lName')
surname.send_keys('szymaniuk2')

email =driver.find_element(By.NAME,'email')
email.send_keys('rafafilm01@hotmail.com2')

#s_button working with xpath 
#s_button =driver.find_element(By.XPATH,'/html/body/form/button')
#s_button.send_keys(Keys.ENTER)

#identify the same button using CSS selector, 2 selectors are in use here (form and button), !! the order matters !! 
s2_button = driver.find_element(By.CSS_SELECTOR,'form button')
s2_button.click()


#can be disabled so the web page does not close off immediately 
driver.close()