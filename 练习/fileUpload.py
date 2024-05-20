import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.get_path import get_path

path = get_path()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/php/fileUpload.htm")

filetest = driver.find_element(By.NAME,'file')
# 可以使用.format引用，r"{}".format(path) 是一个字符串格式化的用法用于文件上传
# filetest.send_keys(r"{}".format(path))
# 也可以使用fr一起使用
# 只有input标签才能这样用
filetest.send_keys(fr"{path}")
driver.find_element(By.NAME,'submit').click()
time.sleep(3)
driver.close()