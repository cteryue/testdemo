import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(option)
driver.get("https://www.baidu.com")
driver.maximize_window()
# ID是以id的方式定位元素
driver.find_element(By.ID,"kw").send_keys("自动化测试")
driver.find_element(By.ID,"su").click()
# time.sleep(5)
# driver.close()