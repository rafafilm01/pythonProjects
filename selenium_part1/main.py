#import webdriver from selenium
from selenium import webdriver

#additional libs needed to access the data from a webpage (2022)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service needs to be pointing to chromedriver module on the disk (or any other driver that will be used )
service = Service('C:\development\chromedriver.exe')

custom_URL='https://www.amazon.pl/Collection-SW852D-Opiekacz-wymienne-Mo%C5%BCliwo%C5%9B%C4%87/dp/B00I64R77Q?ref_=Oct_d_obs_d_20853572031&pd_rd_w=lABvh&pf_rd_p=7e69eec0-e911-4240-88cc-fa0ad7b98dc5&pf_rd_r=4719BAXPKBJDAYKG76WH&pd_rd_r=1c4dc550-4a13-4cc5-9c6b-9125d792d1eb&pd_rd_wg=fLmnf&pd_rd_i=B00I64R77Q'

custom_URL2 ='https://www.python.org/'

#path to the webdriver needs to be provided , the type of webdriver depends on what sort of browser will be used 
chrome_driver_path ='C:\development\chromedriver.exe'

#create the driver based on the browser and the webdriver placed locally 
driver = webdriver.Chrome(service=service)

#open up a website , additional security settgins needed when running from macOS
driver.get(custom_URL)

#find an element based on the class name
price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print("Check", price.tag_name)
#innerHTML is not an attrbibute we can use (such as in example with python.org but the actual content within the HTML tag)
print(price.get_attribute('innerHTML'))

#get the name of the product using an ID
name = driver.find_element(By.ID, 'productTitle')
name_conv =name.get_attribute('innerHTML')
print(f'this is the product description:{name_conv}')


#other ways of finding the elements , sweeping python.org website
driver.get(custom_URL2)

question_bar = driver.find_element(By.NAME, 'q')
#need to specify what attribute we want to pull out from the website , example of the entire element form python.org below:
# <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">
search_bar = question_bar.get_attribute('placeholder')
print(search_bar)
#useful for filling out forms because the names of the forms are later used with javascript, we can tap into the same values and either extract the placeholder text or populate the info from python 

#capture the details of the logo from python website 
logo = driver.find_element(By.CLASS_NAME,'python-logo')
print(logo.size)

#capturing items using 2 or more parameters:
# STILL NEED TO WORK OUT 
# link_from_website =driver.find_element(By.CSS_SELECTOR, 'widget-title a')
# print(link_from_website.text)

#finding an element using xpath 
link_from_website2 =driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[2]/p[2]/a')
#.text on selenium elemnet gets the content of the HTML tag same as .get_attribute('innerHTML')
print(link_from_website2.text)
print('-------------------')
print(link_from_website2.get_attribute('innerHTML'))
# selenium_object.get_attribute('href') to get the actual link
print(link_from_website2.get_attribute('href'))


# will close the website
driver.close()

# will close all tabs and the entire program 
# driver.quit()
# <a href="/downloads/release/python-3102/">Python 3.10.2</a>