import pytest

"""
参数化
"""
# 多参数多次循环
# 运行时，将数组的值分别赋值给变量，每赋值一次，运行一次
@pytest.mark.parametrize("name,word",[["张三","法外狂徒"],["李四","买了否冷"],["王五","我叫王五"]])
def test_01(name,word):
    print(f"我叫{name}，我的台词是：{word}")