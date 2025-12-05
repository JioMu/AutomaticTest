import json


class Test:
    num = 1

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        Test.num += 1

    def countNum(self):
        print(++Test.num)

    def to_json(self):
        return {
            'name': self.name,
            'age': self.age,
            'sex': self.sex
        }

    def convert_to_json(self):
        return json.dumps(self.to_json())


if __name__ == '__main__':
    test = Test("xiaoming", "20", "man")
    print(test.convert_to_json())
    test.countNum()
