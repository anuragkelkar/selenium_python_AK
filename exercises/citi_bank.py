import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get("https://www.online.citibank.co.in/")
browser.maximize_window()
browser.implicitly_wait(20)

browser.find_element(By.XPATH, "//a[@class='newclose']").click()
browser.find_element(By.XPATH, "//a[@class='newclose2']").click()
browser.find_element(By.PARTIAL_LINK_TEXT, "Login").click()

browser.switch_to.window(browser.window_handles[1])
browser.find_element(By.XPATH, "//div[text()=' Forgot User ID? ']").click()

browser.find_element(By.PARTIAL_LINK_TEXT, "select your product type").click()
browser.find_element(By.PARTIAL_LINK_TEXT, "Credit Card").click()
time.sleep(10)
# automate date field using javascript
browser.execute_script("document.querySelector('#bill-date-long').value='24/4/2024'")
# browser.find_element(By.XPATH,"//input[@value='PROCEED']").click()
time.sleep(5)
browser.quit()
