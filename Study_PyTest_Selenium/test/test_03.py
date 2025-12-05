import pytest


def test_s1(login):
    print("用例1，登录之后的其他动作111")


def test_s2(login):
    print("用例2，登录之后的其他动作222")


def test_s3(login):
    print("用例3，登录之后的其他动作333")


if __name__ == '__main__':
    pytest.main(['-s', 'test_03.py'])
