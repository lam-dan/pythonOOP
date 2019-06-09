# Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False
    
    def walk(self):
        return "{} is walking!".format(self.name)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have %s dogs." % (len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

are_my_dogs_hungry = False

for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")

for dog in my_pets.dogs:
    print(dog.walk())

# What’s a class?
# A class is like the blueprint for an object to be created on. It contains attributes, and methods.

# What’s an instance?
# An instance is a copy of the class object in memory.

# What’s the relationship between a class and an instance?
# Instances/objects are created from class blueprints.

# What’s the Python syntax used for defining a new class?
# class PythonClassName:

# What’s the spelling convention for a class name?
# CamelCase notation starting with a capital.

# How do you instantiate, or create an instance of, a class?
# You set the name of a variable and set it equal to the class name followed by an empty parentheses.

# How do you access the attributes and behaviors of a class instance?
# You access attributes and behaviors of a class instance using dot notation

# What’s a method?
# Methods are functions defined inside a class.

# What’s the purpose of self?
# The purpose of self is refers to the current instance of the class. In the _init_ method, self refers to the newly created object;
# while in other methods, self refers to the instance whose method was called.

# What’s the purpose of the __init__ method?
# It intializes an instance of your class, similarly like a constructor that helps you create your object from a class.

# Describe how inheritance helps prevent code duplication.
# Inheritance allows child classes to inherit parent attributes and behaviors.

# Can child classes override properties of their parents?
# Yes.