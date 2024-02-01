import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.medibuddy.in/")
browser.maximize_window()
browser.implicitly_wait(60)

browser.find_element(By.PARTIAL_LINK_TEXT,"Login").click()
browser.find_element(By.XPATH,"//div[text()='I have a Corporate Account']").click()
browser.find_element(By.ID,"corpphone").send_keys("7385825199")
browser.find_element(By.XPATH,"//button[text()='Proceed']").click()
time.sleep(5)
browser.find_element(By.NAME,"otp-field-0").send_keys("8")
browser.find_element(By.NAME,"otp-field-1").send_keys("2")
browser.find_element(By.NAME,"otp-field-2").send_keys("1")
browser.find_element(By.NAME,"otp-field-3").send_keys("9")
browser.find_element(By.XPATH,"//button[text()='Sign In']").click()

browser.find_element(By.PARTIAL_LINK_TEXT,"Login using Username & Password")
browser.find_element(By.NAME,"username").send_keys("john")
browser.find_element(By.XPATH,"//button[text()='Proceed']").click()
browser.find_element(By.NAME,"password").send_keys("john123")
browser.find_element(By.XPATH,"//button[text()='Sign In']").click()

error_msg = browser.find_element(By.XPATH,'//div[@ng-if="isPasswordWrong"]').text
print(error_msg)
browser.quit()