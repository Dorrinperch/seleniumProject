from selenium import webdriver






# 1. open the browser

driver = webdriver.Chrome()
driver.implicitly_wait(40)    #synchronizing the browser
driver.maximize_window()

driver.get("https://www.google.com/")

# 2. open the google.com
#3. search for 'selenium'

driver.find_element_by_id()
# fastest way of fidning element from html document!
driver.find_element_by_name()
driver.find_element_by_class_name()
driver.find_element_by_xpath() # technics, build # technics, build
driver.find_element_by_css_selector() # technics, build # technics, build


driver.find_element_by_link_text()
driver.find_element_()
#4.  capture the result a
# 5. closure the browser


#driver.quit() # close all tabs

#driver.quit() # close all tabs
#driver.close() #closing current tab
#open the google.com

#. Search for 'selenium'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


search_box = driver.find_element(By.NAME, 'q')  # selenium 3, 4

