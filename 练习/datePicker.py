import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/date-picker")


# 单日期选择器，可以直接输入的
# driver.find_element(By.XPATH,'//input[@class = "ivu-input ivu-input-default ivu-input-with-suffix"]').send_keys("2025-12-18")

# 双日期选择器，可以直接输入的
driver.find_elements(By.XPATH,'//input[@class = "ivu-input ivu-input-default ivu-input-with-suffix"]')[1].send_keys("2018-04-03 - 2029-05-16")


time.sleep(3)
driver.close()