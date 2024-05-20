import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com")
driver.maximize_window()

tit = driver.title
print(tit)

cookies = pickle.load(open("D://python-learn//automation_test01//File//cookies.pkl", "rb"))  # 载入cookie
for cookie in cookies:
    cookie_dict = {
        'domain':'.zhihu.com',  # 必须有，不然就是假登录
        'name': cookie.get('name'),
        'value': cookie.get('value')
    }
    driver.add_cookie(cookie_dict)

while driver.title == "知乎 - 有问题，就会有答案":
    print("--请登录--")
    time.sleep(5)


cookie = driver.get_cookies()
print(cookie)
pickle.dump(driver.get_cookies(), open("D://python-learn//automation_test01//File//cookies.pkl", "wb"))



time.sleep(1000)
driver.close()