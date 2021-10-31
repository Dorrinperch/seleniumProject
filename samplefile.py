from selenium import webdriver


driver = webdriver.Chrome()


driver.get("https://www.thelevelupsolutions.com/")
driver.maximize_window()


#driver.quit() # close all tabs


###Web service / API


# Data providers: customers, stock prices, analytical, news
# Service providers: google map, google authenticator, keycloak

# Company A: API (web services)

#a. integrated with company system to provide necessary data for the sytem to operate
#b. bank of america uses location search, they use google map web service


## What is HTML?!
# - Document Object Model - html document ( DOM)
# - tag :
  #  head, body, div button, span, a , input (text, password, submit, checkbox, radio,
  # file, )
# ``` html
#<head> </head>
#<body> </body>
# ```