import json

from common.printable_params import PrintableParams

class ClassA:
    def __init__(self, name, qid):
        self.name = name
        self.qid = qid

    def to_dict(self):
        return {'name': self.name,
                'qid': self.qid}

    @staticmethod
    def from_dict():
        pass

class ClassB:
    def __init__(self, age, name, qid):
        self.age = age
        self.class_a = ClassA(name, qid)

    def to_dict(self):
        return {'age': self.age,
                'class_a': self.class_a.to_dict()}

    @staticmethod
    def from_dict(data_dict: dict) -> "ClassB":
        return ClassB(data_dict['age'], data_dict['class_a']['name'], data_dict['class_a']['qid'])

if __name__ == '__main__':
    c = ClassB(34, 'aaa', 123456)
    print(c.to_dict())

    json_data = json.dumps(c.to_dict())
    loaded_dict = json.loads(json_data)
    d = ClassB.from_dict(loaded_dict)
    assert d.age == c.age
    assert d.class_a.qid == c.class_a.qid
    assert d.class_a.name == c.class_a.name
