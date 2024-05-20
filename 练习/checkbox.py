import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/checkbox")

"""
多选组测试
"""
# XPATH方法定位文字
# driver.find_element(By.XPATH,'//span[text() = "香蕉"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH,'//span[text() = "苹果"]').click()
# time.sleep(2)
# driver.find_elements(By.XPATH,'//span[text() = "西瓜"]')[1].click()

# XPATH方法定位选择项
# driver.find_element(By.XPATH,'//span[text() = "香蕉"]/preceding-sibling::span/input').click()
# driver.find_element(By.XPATH,'//span[text() = "苹果"]/preceding-sibling::span/input').click()
# driver.find_element(By.XPATH,'//span[text() = "西瓜"]/preceding-sibling::span/input').click()

# CSS方法组合定位
driver.find_element(By.CSS_SELECTOR,'input.ivu-checkbox-input[value = "香蕉"]').click()
driver.find_element(By.CSS_SELECTOR,'input.ivu-checkbox-input[value = "苹果"]').click()
driver.find_element(By.CSS_SELECTOR,'input.ivu-checkbox-input[value = "西瓜"]').click()

time.sleep(3)
driver.close()