class Dog:
    species = "Canis familiaris" # Class attribute

    def __init__(self, name, age, breed, species):
        self.name = name
        self.age = age
        self.breed = breed
        self.species = species

    def get_info(self): 
        print(f"The dog's name is {self.name}, age is {self.age}, breed is {self.breed}, species is {self.species}")

d1 = Dog("Tommy", 5, "Labrador", "German Shepherd")
print(d1.species)
d1.get_info()  #always uses the instance attribute when present
print(Dog.species)  #always uses the class attribute


#object introspection (shows all the attributes and methods of the object)
print(dir(d1))
