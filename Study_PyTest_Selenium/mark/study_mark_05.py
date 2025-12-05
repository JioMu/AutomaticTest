import pytest


@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print("登录账户:%s" % user)
    return user


@pytest.fixture(scope="module")
def input_pwd(request):
    pwd = request.param
    print("登录密码:%s" % pwd)
    return pwd


@pytest.mark.parametrize("input_user", ["admin", "test"], indirect=True)
@pytest.mark.parametrize("input_pwd", ["123456", "654321"], indirect=True)
def test_login(input_user, input_pwd):
    input_user = input_user
    input_pwd = input_pwd
    print("测试数据 a-> %s,  b->%s" % (input_user, input_pwd))
    assert input_pwd


if __name__ == '__main__':
    pytest.main(["-s", "test_mark_05.py"])
