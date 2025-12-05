import pytest
import sys

min_version = pytest.mark.skipif(sys.version_info < (3, 12), reason="python版本过低")


@min_version
def test_skipif():
    print("skipif")
