from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(option)
driver.maximize_window()

driver.get("http://www.baidu.com")
# PARTIAL_LINK_TEXT按照链接文本模糊匹配定位，如有复数，支持按照下标定位，只定位可点击的元素
# driver.find_element(By.PARTIAL_LINK_TEXT,"贴吧").click()
driver.find_elements(By.PARTIAL_LINK_TEXT,"贴吧")[0].click()
driver.close()