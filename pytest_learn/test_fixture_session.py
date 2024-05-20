import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# 当scope='session'时，作用范围为整个会话，多个文件只调用一次
# 加上autouse = True时相当于每个方法都要调用这个fixture，方法上不需要传入fixture
# @pytest.fixture()
@pytest.fixture(scope='session')
def driver():
    print("我是前置步骤12+++++++")
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


class Test01:
    def test_fixture1(self,driver):
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(By.CSS_SELECTOR, 'a[href = "http://news.baidu.com"]').text
        button_text = driver.find_element(By.ID, 'su').accessible_name
        assert title == "百度一下，你就知道"
        assert url == 'https://www.baidu.com/'
        assert text == '新闻'
        assert button_text == '百度一下'

    def test_fixture2(self,driver):
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(By.CSS_SELECTOR, 'a[href = "http://news.baidu.com"]').text
        button_text = driver.find_element(By.ID, 'su').accessible_name
        assert title == "百度一下，你就知道"
        assert url == 'https://www.baidu.com/'
        assert text == '新闻'
        assert button_text == '百度一下'

if __name__ == '__main__':
    pytest.main()