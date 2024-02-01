
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://www.facebook.com/")
browser.maximize_window()
browser.implicitly_wait(10)

browser.find_element(By.PARTIAL_LINK_TEXT,"Create new account").click()
browser.find_element(By.NAME,"firstname").send_keys("ak")
browser.find_element(By.NAME,"lastname").send_keys("ttl")
browser.find_element(By.NAME,"reg_email__").send_keys("anuragashwini1618@gmail.com")
browser.find_element(By.NAME,"reg_passwd__").send_keys("lock221B")
browser.find_element(By.XPATH,"//label[text()='Male']").click()

select_day = Select(browser.find_element(By.ID,"day"))
select_day.select_by_visible_text("16")
select_month = Select(browser.find_element(By.ID,"month"))
select_day.select_by_visible_text("Feb")
select_year = Select(browser.find_element(By.ID,"year"))
select_day.select_by_visible_text("1994")

#browser.find_element(By.NAME,"websubmit").click()
