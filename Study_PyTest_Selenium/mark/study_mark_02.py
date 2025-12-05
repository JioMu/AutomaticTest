import pytest


@pytest.mark.webtest
def test_send_http():
    print("send http")
    pass


def test_something_quick():
    print("something quick")
    pass


class TestClass:
    def test_method(self):
        print("method")
        pass


if __name__ == '__main__':
    print("hello  main method")
    pytest.main(["-s", "test_01.py", "-m=not webtest"])
