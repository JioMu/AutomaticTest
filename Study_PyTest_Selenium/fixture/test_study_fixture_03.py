import pytest


@pytest.fixture()
def user():
    print("获取用户信息")
    username = "张三"
    return username


@pytest.fixture()
def password():
    print("获取密码信息")
    password = "123456"
    return password


def test_001(user, password):
    print("\n用例1")
    print("测试账号：%s, 密码：%s" % (user, password))


if __name__ == '__main__':
    pytest.main(["-s", "test_study_fixture_02.py"])
