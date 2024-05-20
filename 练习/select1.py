import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/selectTest.htm")

# 根据定位到的select拿到select对象
select = Select(driver.find_element(By.ID,'s1'))
time.sleep(2)
# select_by_index根据下标选择对应选项，自动选择，不需要点击事件
select.select_by_index(2)
time.sleep(2)

# select_by_value根据value值来选择对应的选项，自动选择，不需要点击事件
select.select_by_value("49")
time.sleep(2)

# select_by_visible_text根据实际看到的内容来选择对应的选项，自动选择，不需要点击事件
select.select_by_visible_text("Email")


time.sleep(3)
driver.close()