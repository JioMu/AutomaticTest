import pytest


@pytest.fixture()
def user():
    print("获取用户信息")
    username = "张三"
    password = "123456"
    return [username, password]


def test_001(user):
    print("\n用例1")
    username = user[0]
    password = user[1]
    print("测试账号：%s, 密码：%s" % (username, password))


if __name__ == '__main__':
    pytest.main(["-s", "test_study_fixture_02.py"])
