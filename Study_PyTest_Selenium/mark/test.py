from mymodule.test_001 import min_version
import pytest


@min_version
def test_001():
    print("test_001")
