# test_10.py
import pytest


@pytest.mark.webtest
def test_send_http():
    print("send http")
    pass


@pytest.mark.quick
def test_something_quick():
    print("something quick")
    pass


@pytest.mark.TestClass
class TestClass:
    @pytest.mark.TestMethod
    def test_method(self):
        print("test method")
        pass


if __name__ == '__main__':
    print("main")
    pytest.main(['-m webtest'])
