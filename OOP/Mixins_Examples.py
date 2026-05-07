import json
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SerializerMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.__dict__)

class Employee(SerializerMixin, Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

if __name__ == '__main__':
    john = Employee("John Doe", 30, 50000)
    print(john.to_json())
    print(john.to_pickle())