from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

keyword = input("수집할 이미지 : ")

url = "https://search.naver.com/search.naver?ssc=tab.image.all&where=image&query={}".format(keyword)
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()


driver.get(url)

time.sleep(3)
driver.quit()