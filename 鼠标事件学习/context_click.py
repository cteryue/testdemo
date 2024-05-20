import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')
driver.maximize_window()

location = driver.find_element(By.CSS_SELECTOR,'a[href = "https://www.douban.com/explore/"]')
# 拿到鼠标对象
action = ActionChains(driver)

# context_click()鼠标右击事件
action.context_click(location).perform()


time.sleep(4)
driver.close()