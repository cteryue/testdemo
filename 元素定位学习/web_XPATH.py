import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

# 根据绝对定位
# driver.find_element(By.XPATH,"/html/body/div/div/div[3]/a[2]").click()

# 根据ID定位
# driver.find_element(By.XPATH,"//input[@id='kw']").send_keys("124")

# 根据class定位
# driver.find_element(By.XPATH,"//input[@class = 's_ipt']").send_keys("124")

# 根据name定位
# driver.find_element(By.XPATH,"//input[@name = 'wd']").send_keys("ces")

# 多个属性组合定位
# driver.find_element(By.XPATH,"//input[@id = 'kw' and @name = 'wd' and @class = 's_ipt']").send_keys("ces1")

# 多组数据下标
# driver.find_element(By.XPATH,'//div[@id = "s-top-left"]/a[2]').click()

# 通过子元素找父元素,..代表上一级
# driver.find_element(By.XPATH,'//div[@id = "s-top-left"]/../div[3]/a[1]').click()

# 通过span文本定位
# driver.find_element(By.XPATH,'//span[text()="总书记的一周"]').click()

# 通过文本包含
# driver.find_element(By.XPATH,'//span[contains(text(),"男子")]').click()

# 通过同级弟弟定位
# driver.find_element(By.XPATH,'//div[@id ="s-top-left" ]/a/following-sibling::a[6]').click()

# 通过同级哥哥定位
driver.find_element(By.XPATH,'//div[@id ="s-top-left" ]/a/following-sibling::a[6]/preceding-sibling::a[3]').click()

time.sleep(3)
driver.close()