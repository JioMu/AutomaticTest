import pytest


@pytest.mark.parametrize('x', [1, 2, 3])
@pytest.mark.parametrize('y', [4, 5, 6])
def test_foo(x, y):
    print("test")


if __name__ == '__main__':
    print("测试数据组合")
    pytest.main(['-s', 'test_08.py'])
