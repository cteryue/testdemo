import time
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.douban.com/')
time.sleep(2)

# 需要执行的js语句
js_down = "window.scrollTo(0, 10000)"

# execute_script执行js语句
driver.execute_script(js_down)
time.sleep(2)
driver.close()



