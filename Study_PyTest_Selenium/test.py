import chardet

with open("pytest.ini", "rb") as f:
    print(chardet.detect(f.read()))  # 输出如 {'encoding': 'utf-8', 'confidence': 0.99}
