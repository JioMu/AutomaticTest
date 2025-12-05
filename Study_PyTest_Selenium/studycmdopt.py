import pytest


def test_answer(cmdopt):
    if cmdopt == "type1":
        print("cmdopt is type1")
    elif cmdopt == "type2":
        print("cmdopt is type2")


if __name__ == "__main__":
    pytest.main(["-s", "studycmdopt.py"])
