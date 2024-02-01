import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://google.com/")
#driver.find_element(By.XPATH, "//div[text()='Accept all']").click()
action = webdriver.ActionChains(driver)
(action.click(driver.find_element(By.NAME, "q")).pause(1)
 .key_down(Keys.SHIFT).send_keys("hello world").key_up(Keys.SHIFT).pause(1)
 .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).pause(1)
 .send_keys(Keys.ENTER).perform()
 )

time.sleep(10)
driver.quit()
