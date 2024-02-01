import time

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get("http://demo.openemr.io/b/openemr/")
browser.maximize_window()
browser.implicitly_wait(30)

browser.find_element(By.ID,"authUser").send_keys("admin")
browser.find_element(By.ID,"clearPass").send_keys("pass")
select_day = Select(browser.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_day.select_by_value("18")
browser.find_element(By.ID,"login-button").click()

patient= browser.find_element(By.XPATH,"//div[text()='Patient']")
hover=action_chains.ActionChains(browser).move_to_element(patient)
hover.perform()

browser.find_element(By.XPATH,"//div[text()='New/Search']").click()

browser.switch_to.frame(browser.find_element(By.NAME,"pat"))
browser.find_element(By.NAME,"form_fname").send_keys("A")
browser.find_element(By.NAME,"form_lname").send_keys("B")
browser.find_element(By.NAME,"form_DOB").send_keys("01/02/2024")
select_gender = Select(browser.find_element(By.NAME,"form_sex"))
select_gender.select_by_visible_text("Male")
browser.find_element(By.NAME,"create").click()

browser.switch_to.default_content()
browser.switch_to.frame(browser.find_element(By.ID,"modalframe"))
browser.find_element(By.XPATH,"//button[text()='Confirm Create New Patient']").click()
time.sleep(2)

browser.quit()