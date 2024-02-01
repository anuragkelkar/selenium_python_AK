import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://netbanking.hdfcbank.com/netbanking/")

#frame switch
frame_login=driver.find_element(By.NAME,"login_page")
driver.switch_to.frame(frame_login)
driver.find_element(By.NAME,"fldLoginUserId").send_keys("jack")
driver.find_element(By.PARTIAL_LINK_TEXT,"CONTINUE").click()
driver.switch_to.default_content()
time.sleep(2)
driver.quit()