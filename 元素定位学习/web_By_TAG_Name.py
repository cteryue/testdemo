from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(option)
driver.maximize_window()

driver.get("http://www.bilibili.com")
# TAG_NAME是以标签的方式定位元素
driver.find_element(By.TAG_NAME,"input").send_keys("selenium")
