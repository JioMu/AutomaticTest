import pytest


@pytest.fixture(scope="function")
def start(request):
    print("\n————开始执行测试用例————")


def test_a(start):
    print("\n————执行测试用例a————")


class Test_aaa:
    def test_01(self, start):
        print("\n————执行测试用例01————")

    def test_02(self, start):
        print("\n————执行测试用例02————")
