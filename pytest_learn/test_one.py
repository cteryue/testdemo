"""
测试类必须以Test，并且不能有init方法
"""
import pytest


class TestCase:
    def test_01(self):
        name = "测试"
        assert name == "测试"

    def test_02(self):
        num = 10
        assert num == 10

    def test_03(self):
        num = 11
        assert num == 11

if __name__ == '__main__':
    pytest.main()