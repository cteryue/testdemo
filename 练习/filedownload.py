import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.get_path import get_path, download_path, del_file

path2 = del_file()

# os.path.exists(path2)判断path2是否存在
if os.path.exists(path2):
    os.remove(path2)
path1 = download_path()

# 实例化初始游览器对象
options = webdriver.ChromeOptions()
# 设置下载地址
prefs = {"download.default_directory": f"{path1}"}
# prefs自定义偏好设置
options.add_experimental_option("prefs",prefs)


path = get_path()
driver = webdriver.Chrome(options)
driver.maximize_window()
driver.get("https://registry.npmmirror.com/binary.html?path=chromedriver/")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'a[href = "https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE"]').click()

time.sleep(3)
driver.close()