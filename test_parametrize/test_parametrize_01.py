import pytest

"""
参数化
"""
# 单参数多次循环
# 运行时，将数组的值分别赋值给变量，每赋值一次，运行一次
@pytest.mark.parametrize("name",["张三","李四","王五"])
def test_01(name):
    assert name == "张三"