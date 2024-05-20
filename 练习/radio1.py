import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/radio")

# driver.find_elements(By.XPATH,'//input[@type = "radio" and @class = "ivu-radio-input" ]')[2].click()
# driver.find_element(By.XPATH,'//span[text() = "Android"]').click()
# driver.find_element(By.XPATH,'//span[text() = "Windows"]').click()

"""
单选组测试
"""

# XPATH方法
# driver.find_element(By.XPATH,'//span[text() = "Android" ]/preceding-sibling::span/input').click()
# driver.find_element(By.XPATH,'//div[@class = "i-demo-run"]/div/div/label/span[text() = "Windows"]/../span/input').click()
# driver.find_element(By.XPATH,'//div[@class = "i-demo i-article-anchor" and @data-title="组合使用"]/div/div/div[1]/div/div/div[2]/div/label[3]/span/input').click()


# CSS方法
# driver.find_element(By.CSS_SELECTOR,'.ivu-radio-group.ivu-radio-group-default.ivu-radio-default.ivu-radio-group-vertical>label:nth-child(3)>span>input').click()
# driver.find_element(By.CSS_SELECTOR,'.i-demo.i-article-anchor#group>div>div>div:nth-child(1)>div>div>div:nth-child(2)>div>label:nth-child(3)>span>input').click()


time.sleep(3)
driver.close()