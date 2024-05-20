import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,'a[href = "https://movie.douban.com"]').click()

# driver.current_window_handle获取当前窗口对象
a = driver.current_window_handle
print(a)
time.sleep(2)

# driver.window_handles获取所有窗口对象
b = driver.window_handles
print(b)
time.sleep(2)

# driver.switch_to.window()跟据入参对象切换到对应窗口
driver.switch_to.window(b[0])
time.sleep(2)
driver.close()
