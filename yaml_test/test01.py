import time
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

# 从yaml文件中拿数据
# Loader=yaml.FullLoader使用了PyYAML提供的FullLoader解析器。FullLoader是一个更加安全的加载器，它可以防止代码注入攻击
# with open('..//config//test01.yaml', 'r') as f:
#     data = yaml.load(f,Loader=yaml.FullLoader)

# 如果不指定Loader参数，默认使用的是SafeLoader加载器，但在PyYAML的新版本中，SafeLoader已经被标记为不安全，建议使用FullLoader
with open("..//config//test01.yaml",encoding="utf-8") as f:
    data = yaml.safe_load(f)

path = data['path']
id = data['id']



driver = webdriver.Chrome()
driver.maximize_window()
driver.get(path)

driver.find_element(By.CSS_SELECTOR,id).send_keys("测试")

time.sleep(2)
driver.close()



