import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')
driver.maximize_window()

driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys("1241243")
time.sleep(2)

# Keys.ENTER键盘的回车事件
# driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.ENTER)
# time.sleep(2)

# Keys.BACK_SPACE键盘的删除事件
# driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.BACK_SPACE)
# time.sleep(2)

# Keys.SPACE键盘的空格事件
# driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.SPACE)
# time.sleep(2)

# Keys.ESCAPE键盘的回退键
# driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.ESCAPE)
# time.sleep(2)

# Keys.TAB键盘的制表键
# driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.TAB)
# time.sleep(2)

# send_keys(Keys.CONTROL,"a")键盘的全选
driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.CONTROL,"a")
time.sleep(2)

# send_keys(Keys.CONTROL,"c")键盘的复制
driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.CONTROL,"c")
time.sleep(2)

# send_keys(Keys.BACK_SPACE)键盘的删除
driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.BACK_SPACE)
time.sleep(2)

# send_keys(Keys.CONTROL,"v")键盘的粘贴
driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.CONTROL,"v")
time.sleep(2)

# send_keys(Keys.CONTROL,"v")键盘的全选
driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.CONTROL,"a")
time.sleep(2)

# send_keys(Keys.CONTROL,"x")键盘的剪切
driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.CONTROL,"x")
time.sleep(2)

# send_keys(Keys.CONTROL,"v")键盘的粘贴
driver.find_element(By.XPATH,'//input[@name = "q"]').send_keys(Keys.CONTROL,"v")
time.sleep(2)
driver.close()