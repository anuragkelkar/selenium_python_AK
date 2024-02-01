import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://datatables.net/extensions/select/examples/initialisation/checkbox.html")
time.sleep(2)

# find count of rows in table to iterate through all 6 tables
for y in range(1, 7):
    driver.find_element(By.XPATH,f"//a[text()='{y}']").click()
    count_rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
    number_of_rows = len(count_rows)
    for i in range(1, number_of_rows+1):
        name1 = driver.find_element(By.XPATH, f"//table[@id='example']/tbody/tr[{i}]/td[2]").text
        print(name1)
# Click on the checkbox when name is matching with "Brenden Wagner"

"""for i in range(1, number_of_rows):
    name1 = driver.find_element(By.XPATH, f"//table[@id='example']/tbody/tr[{i}]/td[2]").text
    if "Brenden Wagner" == name1:
        driver.find_element(By.XPATH,f"//table[@id='example']/tbody/tr[{i}]/td[1]").click()
        break"""


