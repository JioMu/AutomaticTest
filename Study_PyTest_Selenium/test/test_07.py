import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.param("6*9", 42, marks=pytest.mark.xfail(reason="known bug")),  # 使用 pytest.param 标记预期失败的测试用例
])
def test_eval(test_input, expected):
    print("--测试开始--")
    assert eval(test_input) == expected


if __name__ == "__main__":
    pytest.main(["-s", "test_07.py"])
