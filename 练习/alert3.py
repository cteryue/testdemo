import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/promptTest.htm")

driver.find_element(By.NAME,'b1').click()
time.sleep(2)

# 在弹窗的输入框中输入文字，但是没有显示输入的数据
driver.switch_to.alert.send_keys("测试")
time.sleep(2)

# 点击确定，关闭弹窗
driver.switch_to.alert.accept()

# 点击取消，关闭弹窗
# driver.switch_to.alert.dismiss()

time.sleep(3)
driver.close()