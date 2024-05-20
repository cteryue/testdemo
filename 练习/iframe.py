import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/iframesTest.htm")
time.sleep(2)
driver.find_element(By.ID,'checkRecord').clear()
time.sleep(2)
driver.find_element(By.ID,'checkRecord').send_keys("123")
# 使用下标的方式进入iframe
# driver.switch_to.frame(0)
# driver.find_element(By.CSS_SELECTOR,'a[href = "index.htm"]').click()

# 使用元素定位的方式进入iframe
iframe1 = driver.find_element(By.CSS_SELECTOR,'body>iframe')


driver.switch_to.frame(iframe1)
driver.find_element(By.CSS_SELECTOR,'a[href="linkTest.htm"]').click()

# 退回到到上一级，退出iframe
driver.switch_to.default_content()
driver.find_element(By.ID,'checkRecord').clear()
time.sleep(2)
driver.find_element(By.ID,'checkRecord').send_keys("666")

# 切换到主页面，退出iframe
driver.switch_to.parent_frame()
driver.find_element(By.ID,'checkRecord').clear()
time.sleep(2)
driver.find_element(By.ID,'checkRecord').send_keys("111")



time.sleep(2)
driver.close()
