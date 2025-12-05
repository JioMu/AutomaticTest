import pytest

CanShu = [{"user": "admin", "pwd": "::"}]


@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    pwd = request.param["pwd"]
    print("正在登录,账号:%s,密码:%s" % (user, pwd))
    if pwd == "123456":
        return True
    else:
        return False


@pytest.mark.parametrize("login", CanShu, indirect=True)
class TestLogin:
    def test_01(self, login):
        print("测试用例01")
        result = login
        print("登录结果为：%s" % result)
        assert result is True

    def test_02(self, login):
        print("测试用例02")
        result = login
        print("登录结果为：%s" % result)
        if not result:
            pytest.xfail("登录失败，跳过用例，标记为fail")
        assert 1 == 1

    def test_03(self, login):
        print("测试用例03")
        result = login
        print("登录结果为：%s" % result)
        if not result:
            pytest.xfail("登录失败，跳过用例，标记为fail")
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(["-s", "study_mark_03.py"])
