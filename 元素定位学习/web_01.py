import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 与游览器建立链接，并且获取实例对象
driver = webdriver.Chrome()

# 跳转对应页面
driver.get("https://www.bilibili.com")

# 通过class_name获取元素的名称，send_keys输入框输入的参数
driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys("自动化测试")

# click单击事件
driver.find_element(By.CLASS_NAME,"nav-search-btn").click()
time.sleep(5)
driver.close()