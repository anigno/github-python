import AnonObject


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{0} is {1} years old".format(self.name, self.age)

    def __repr__(self):
        return self.__str__()


people = [
    Person("roni", 46),
    Person("Julia", 25),
    Person("boris", 23),
    Person("elad", 40)
]

ageQuery = [
    AnonObject.AnonimousObject(name=p.name, age=p.age)
    for p in people
    if p.age >= 25
]

sortedQuery = sorted(ageQuery, key=lambda p: -p.age, reverse=False)

for p in people:
    print(p)

print(ageQuery)

print(sortedQuery)
