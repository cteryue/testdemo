import pytest

# 直接写@pytest.fixture()相当于默认为scope='function'，当scope='function'时，作用范围每次调用方法时都调用前置方法
# 加上autouse = True时相当于每个方法都要调用这个fixture，方法上不需要传入fixture
# @pytest.fixture()
@pytest.fixture(scope='function',autouse=True)
def fixture1():
    print("我是前置步骤1+++++++")
    return 11

@pytest.fixture(scope='function')
def fixture2():
    print("我是前置步骤2+++++++")
    return 11

def test_fixture1(fixture2):
    assert fixture2 == 11

def test_fixture2():
    assert 11 == 11