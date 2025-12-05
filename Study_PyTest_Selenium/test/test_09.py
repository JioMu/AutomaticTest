import pytest
from mymodule.test_001 import min_version


@pytest.mark.skip(reason="此条用例不执行")
def test_skip():
    print("skip")


@min_version
def test_skipif():
    print("skipif")
