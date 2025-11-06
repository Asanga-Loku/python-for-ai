#parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
# Child class inheriting everything from Animal 
# and add its own method.
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
    
#create an instance of a cat
#but not of an Animal. Animal (parent) class can have common
#things for all animals. Then individual child class
#can add animal types
my_cat = Cat("Missy")
my_cat2 = Cat("Sneaky")

print(my_cat.eat())
print(my_cat.sleep())
print(my_cat.speak())
print(f"\n{my_cat2.speak()}")
#I've used \n to have a new line feed for the last one

"""let's try something tricker.. can we edit the values of the parent from child?"""

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Pass name to parent's __init__
        self.breed = breed      # Dog-specific attribute
    
    def describe(self):
        return f"{self.name} is a {self.breed}"

# Create dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriever")

# Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe())  # Buddy is a Golden Retriever
print(golden.is_pet)      # True (inherited from Animal)



"""another level down here... overriding paren't methods"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"

# Different animals, different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.make_sound())  # Something makes a sound
print(dog.make_sound())      # Buddy barks: Woof!
print(cat.make_sound())      # Whiskers meows: Meow!