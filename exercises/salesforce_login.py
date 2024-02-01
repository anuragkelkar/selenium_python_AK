import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
browser.maximize_window()
browser.implicitly_wait(10)

browser.find_element(By.XPATH,"//button[text()='Accept All Cookies']").click()
browser.find_element(By.NAME,"UserFirstName").send_keys("John")
browser.find_element(By.NAME,"UserLastName").send_keys("Wick")
browser.find_element(By.NAME,"UserEmail").send_keys("john@gmail.com")
browser.find_element(By.NAME,"UserEmail").send_keys("john@gmail.com")

select_title = Select(browser.find_element(By.NAME,"UserTitle"))
select_title.select_by_visible_text("IT Manager")
select_emp_nos = Select(browser.find_element(By.NAME,"CompanyEmployees"))
select_emp_nos.select_by_visible_text("201 - 500 employees")
select_country = Select(browser.find_element(By.NAME,"CompanyCountry"))
select_country.select_by_value("GB")

#browser.find_element(By.PARTIAL_LINK_TEXT,"Main Services Agreement").click()
browser.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
browser.quit()