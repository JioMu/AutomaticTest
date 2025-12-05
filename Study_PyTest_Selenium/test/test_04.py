import pytest


@pytest.fixture(scope='module')
def open():
    print("\n打开浏览器\n")
    yield
    print("执行teardown")
    print("\n关闭浏览器")


def test_case1(open):
    raise NameError("用例1出错")


def test_case2(open):
    print("用例2")


def test_case3(open):
    print("用例3")


if __name__ == '__main__':
    pytest.main(['-s', 'test_04.py'])
