import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.db4free.net/")
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,"input_username").send_keys("anurag")
driver.find_element(By.ID,"input_password").send_keys("ak123")
driver.find_element(By.ID,"input_go").click()
#error = driver.find_element(By.XPATH,"//*[contains(text(),'Error')]").text
error = driver.find_element(By.ID,"pma_errors").text
print(error)
driver.close()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
driver.quit()