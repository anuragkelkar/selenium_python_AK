import time

from selenium import webdriver

#create object of class webdriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
print(driver.title)
print(driver.current_url)

time.sleep(5)
driver.quit()