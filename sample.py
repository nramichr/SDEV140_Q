class Person :
    def __init__(self, name, age):
        self._name = name
        self._age = age 

    def greet (self):
        print(f"Hello, my name is {self._name} and I am {self._age} years old.")

my_person = Person("Alice", 30)
print(my_person._name)
print(my_person._age)
my_person.greet()
