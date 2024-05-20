import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

# CSS_SELECTOR之根据ID定位元素，需要在ID前面加上#
# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("selenium")
# driver.find_element(By.CSS_SELECTOR,"#su").click()

# 根据CLASS属性值定位
# driver.find_element(By.CSS_SELECTOR,".nav-search-input").send_keys("ces")
# driver.find_element(By.CSS_SELECTOR,".nav-search-btn").click()

# 根据name定位，需要注意：外层双引号，内层单引号，或者外单内双
# driver.find_element(By.CSS_SELECTOR,'[name = "wd"]').send_keys("qwe")

# 根据标签属性定位
# driver.find_element(By.CSS_SELECTOR,'a[href = "http://map.baidu.com"]').click()

# 模糊匹配——包括
# driver.find_element(By.CSS_SELECTOR,'a[href*= "map.baidu.com"]').click()

# 模糊匹配——匹配开头
# driver.find_element(By.CSS_SELECTOR,'a[href^= "http://map.baidu"]').click()

# 组合定位
# driver.find_element(By.CSS_SELECTOR,"input.s_ipt").send_keys("组合定位")

"""
定位子元素可以使用F12里面找到对应元素，右键点击复制selector直接粘贴就能用
缺点：易读性太差，一般都很长
"""
# 定位子元素
# driver.find_element(By.CSS_SELECTOR,"div#s-top-left>a").click()

# 若id或者class唯一，可以省略div
# driver.find_element(By.CSS_SELECTOR,"div#s-top-left>a").click()
# driver.find_element(By.CSS_SELECTOR,"#s-top-left>a").click()

# 使用class
# driver.find_element(By.CSS_SELECTOR,"div.s-top-left-new.s-isindex-wrap>a").click()
# driver.find_element(By.CSS_SELECTOR,".s-top-left-new.s-isindex-wrap>a").click()
driver.find_element(By.CSS_SELECTOR,".s-top-left-new.s-isindex-wrap>a:nth-child(3)").click()
# driver.find_elements(By.CSS_SELECTOR,".s-top-left-new.s-isindex-wrap>a")[2].click()
# driver.find_element(By.CSS_SELECTOR,".s-top-left-new.s-isindex-wrap>a:first-child").click()

# 下面是右键复制的
# driver.find_element(By.CSS_SELECTOR,"#hotsearch-content-wrapper > li:nth-child(2) > a > span.title-content-title").click()


time.sleep(3)
driver.close()