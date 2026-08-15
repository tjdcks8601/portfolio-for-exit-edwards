from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # 실무기준
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.google.com")

print(driver.title)

stp1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gb"]/div[1]/div[1]/a')))
stp1.click()

time.sleep(5)
driver.quit()
