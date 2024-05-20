import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/select")

# 通过点击事件来实现选择框的选择
driver.find_elements(By.XPATH,'//span[@class = "ivu-select-placeholder" and text() = "请选择"]')[0].click()
driver.find_elements(By.XPATH,'//ul[@class = "ivu-select-dropdown-list"]/li[text() = "London"]')[0].click()


time.sleep(3)
driver.close()