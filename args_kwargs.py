class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed,*args, **kwargs):
        super().__init__(name)
        self.breed = breed 
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador", 1, 2, 3, color="black", age =5)