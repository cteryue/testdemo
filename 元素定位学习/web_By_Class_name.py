import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 不让游览器自动关闭
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(option)
driver.get("http://www.bilibili.com")
# 最大化游览器
driver.maximize_window()
# CLASS_NAME是以class的方式定位元素
# 若Class_name有多个相同元素名称，可以通过find_elements去根据下标找到对应的元素
# 若不根据下标，则默认找到第一个，不支持带空格的元素定位，会报错
driver.find_elements(By.CLASS_NAME,"channel-link")[23].click()
for a in driver.find_elements(By.CLASS_NAME,"channel-link"):
    print(a.text)
