from selenium import webdriver
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

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img.__fe_image_tab_content_thumbnail_image'))
    )
except Exception as e:
    print(f"요소 로드 실패: {e}")

for _ in range(5):
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(0.5)

imgs = driver.find_elements(By.CSS_SELECTOR, 'img.__fe_image_tab_content_thumbnail_image')
print(f"찾은 이미지: {len(imgs)}개")

time.sleep(3)
driver.quit()