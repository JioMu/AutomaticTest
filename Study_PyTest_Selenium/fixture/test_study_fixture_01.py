import pytest


@pytest.fixture
def user():
    print("获取用户名")
    username = "mjy"
    assert username == "lhx"  # 此处断言失败为failed
    return username


def test_01(user):
    assert user == "lhx"  # 此处断言失败为error


if __name__ == '__main__':
    pytest.main(["-s", "test_study_fixture_01.py"])
