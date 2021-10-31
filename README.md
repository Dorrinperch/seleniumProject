# Title of the page
## Title 2 text
### Title 3


# Selenium WebDriver( full name of the selenium) with python 

## Selenium setup
1. downland selenium
go to the Terminal (pycharm)
    ``` python
    pip install selenium # library, code  written by developers to build, open source
   pip freeze # to check the selenium is in the list 
    ```
2. download chromedriver
   - check 
3. save i the Python main location
4. import selenium, run sample code

from selenium import webdriver






# 1. open the browser

driver = webdriver.Chrome()
driver.implicitly_wait(40)    #synchronizing the browser
driver.maximize_window()

driver.get("https://www.thelevelupsolutions.com/")

# 2. open the google.com
#3. search for 'selenium'
#4.  capture the result a
# 5. closure the browser


#driver.quit() # close all tabs
#driver.close() closing current tab
#open the google.com
driver.get()