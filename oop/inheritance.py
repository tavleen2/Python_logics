class Animal:   # Parent class(superclass)
    location = "Canada"
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Speaking now.....")

class Dog(Animal):
    def speak(self):
        # super().speak()  #calling the parent class method
        print("Woof!!")


# a = Animal("Dog")
# a.speak()
d = Dog("Tommy")
print(d.name)
d.speak()
print(d.location)  #inherited attribute