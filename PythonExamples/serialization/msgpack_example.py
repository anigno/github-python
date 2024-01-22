import msgpack

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_msgpack(self):
        return {"name": self.name, "age": self.age}

    @classmethod
    def from_msgpack(cls, data):
        return cls(**data)

class Family:
    def __init__(self, members):
        self.members = members

    def to_msgpack(self):
        return {"members": [person.to_msgpack() for person in self.members]}

    @classmethod
    def from_msgpack(cls, data):
        members = [Person.from_msgpack(person_data) for person_data in data["members"]]
        return cls(members)

# Create instances of Person
person1 = Person(name='Alice', age=30)
person2 = Person(name='Bob', age=35)
person3 = Person(name='Charlie', age=10)

# Create an instance of Family containing Person instances
family_instance = Family(members=[person1, person2, person3])

# Serialize the data to MessagePack
serialized_data = msgpack.packb(family_instance.to_msgpack())

# Deserialize the data
loaded_data = msgpack.unpackb(serialized_data, raw=False)

# Create an instance of Family from the loaded data
loaded_family_instance = Family.from_msgpack(loaded_data)

# Access the loaded instance
for person in loaded_family_instance.members:
    print(f"Name: {person.uav_descriptor}, Age: {person.age}")
