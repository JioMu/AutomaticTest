import pytest


@pytest.mark.smoke
class TestLogin:
    """登录测试类"""

    @pytest.mark.smoke
    @pytest.mark.success
    def test_login_success(self):
        """登录成功"""
        print("登录成功")
        pass

    @pytest.mark.failed
    def test_login_fail(self):
        """登录失败"""
        print("登录失败")
        pass


@pytest.mark.logout
class TestLogout:
    """登出测试类"""

    @pytest.mark.smoke
    @pytest.mark.success
    def test_logout_success(self):
        """登出成功"""
        print("登出成功")
        pass

    @pytest.mark.failed
    def test_logout_fail(self):
        """登出失败"""
        print("登出失败")
        raise Exception("登出失败")
