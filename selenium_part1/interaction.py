#objective open up URL and get the total number of articles form the website 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('C:\development\chromedriver.exe')
URL = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome(service=service)

#open web page 
driver.get(URL)


#get the data using HTML / CSS tags, be sure to mark down ID itmes with # and class items with . when marking down items  for search !!! 
no_of_articles_1 =driver.find_element(By.CSS_SELECTOR,'#articlecount a')

#get the data using xpath
no_of_articles =driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')



print(f'total number of articles is : {no_of_articles_1.text}')
print('-----------')
print(f'total number of articles is: {no_of_articles.text}')

#click action on an element using link_by_text
all_portals =driver.find_element_by_link_text('All portals')
#all_portals.click()

#populate type fields 
#ist identify the filed that is going to be edited 
edit_field =driver.find_element_by_name('search')
edit_field.send_keys('conan the barbarian')
#separate  selenium import needed to program function keys (like enter etc)
edit_field.send_keys(Keys.ENTER)
#driver.close()