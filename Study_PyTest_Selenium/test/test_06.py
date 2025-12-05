import pytest


@pytest.fixture(scope="module", autouse=True)
def start(request):
    print("\n开始执行module")
    print("module      :  %s" % request.module.__name__)
    print("启动浏览器")
    yield
    print("结束测试!")


class Test_aaa:
    @pytest.fixture(scope="function", autouse=True)
    def open_home(self, request):
        print("\n-----回到首页------")

    @pytest.mark.skip(reason=f"test_01用例不执行")
    def test_01(self):
        print("---------用例1-------------")

    def test_02(self):
        print("---------用例2-------------")
