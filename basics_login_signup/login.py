import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.facebook.com/")

browser.find_element(By.ID, "email").send_keys("anuragdkelkar@gmail.com")
browser.find_element(By.ID, "pass").send_keys("lock221B")
browser.find_element(By.NAME, "login").click()
time.sleep(25)
if browser.find_element(By.ID,"error_box").is_displayed() :
    print("login fail")
else :
    print("login successful")
