class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
myobj=Person("Samuel", 20)
myobj2=Person("Janet", 13)
myobj3=Person("Cindy", 60)
myobj4=Person("James", 27)
myobj5=Person("Malia", 10)

myobj.show()
myobj2.show()
myobj3.show()
myobj4.show()
myobj5.show()