from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(option)
driver.maximize_window()

driver.get("http://www.baidu.com")
# NAME按照name去定位，如有复数，支持按照下标定位，用的不多
driver.find_element(By.NAME,"wd").send_keys("根据Name定位")

