import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')
driver.maximize_window()

# 定位到需要悬停的元素
location = driver.find_element(By.CSS_SELECTOR,'.site-name')

# 初始化一个ActionChains(driver)类
action = ActionChains(driver)

# 对定位的元素执行悬停操作
# perform()：执行所有ActionChains中存储的行为
action.move_to_element(location).perform()

time.sleep(4)
driver.close()










