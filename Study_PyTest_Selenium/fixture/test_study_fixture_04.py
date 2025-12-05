import pytest
import allure


@pytest.fixture()
def first_fixture():
    print("获取用户名")
    username = "admin"
    return username


@pytest.fixture()
def second_fixture(first_fixture):
    print("获取密码")
    username = first_fixture
    password = "123456"
    return [username, password]


@allure.story("获取用户名")
def test_getUser(second_fixture):
    with allure.step("获取用户名"):
        print("\n测试账户: %s, 登录密码: %s" % (second_fixture[0], second_fixture[1]))


if __name__ == '__main__':
    pytest.main(["-s", "test_study_fixture_04.py"])
