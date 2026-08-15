from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

keyword = input("수집할 이미지 : ")

url = "https://search.naver.com/search.naver?ssc=tab.image.all&where=image&query={}".format(keyword)
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(url)

time.sleep(3)
driver.quit()