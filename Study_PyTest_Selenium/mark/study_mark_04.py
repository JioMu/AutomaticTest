import pytest


@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    pwd = request.param["pwd"]
    print("登录：%s %s" % (user, pwd))
    if pwd:
        return True
    else:
        return False


@pytest.mark.parametrize("login", [{"user": "admin", "pwd": "123456"}, {"user": "admin", "pwd": ""}], indirect=True)
def test_login(login):
    result = login
    print("测试用例中login返回值: %s" % result)
    assert result, "登录失败"


if __name__ == '__main__':
    pytest.main(["-s", "test_study_mark_04.py"])
