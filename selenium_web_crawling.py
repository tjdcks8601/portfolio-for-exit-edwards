from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # 실무기준
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.samsung.com")

print(driver.title)

stp1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header__navi"]/div[1]/div/div[3]/div/div[6]/button')))
stp1.click()

stp2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[2]/label/span[1]')))
stp2.click()

time.sleep(5)
driver.quit()
