import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demos.telerik.com/kendo-ui/dragdrop/index')
driver.maximize_window()
time.sleep(20)

location1 = driver.find_element(By.XPATH,'//div[@id = "draggable" and @data-role = "draggable"]')
location2 = driver.find_element(By.XPATH,'//div[@id = "droptarget" and @data-role = "droptarget"]')
action = ActionChains(driver)

# 鼠标拖动，从location1拖到location2
action.drag_and_drop(location1,location2).perform()

time.sleep(4)
driver.close()