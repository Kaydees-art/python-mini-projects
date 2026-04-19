# TYPES OF INHERITANCE IN PYTHON — Animal Examples


# 1. SINGLE INHERITANCE
# One child class inherits from one parent class.

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f"{self.name} breathes air."

    def eat(self):
        return f"{self.name} eats food."


class Dog(Animal):
    def bark(self):
        return f"{self.name} says: Woof! Woof!"


dog = Dog("Rex")
print(dog.breathe())
print(dog.eat())
print(dog.bark())


# 2. MULTIPLE INHERITANCE
# One child class inherits from more than one parent class.

class Swimmer:
    def swim(self):
        return f"{self.name} is swimming."


class Runner:
    def run(self):
        return f"{self.name} is running."


class Duck(Animal, Swimmer, Runner):
    def quack(self):
        return f"{self.name} says: Quack! Quack!"


duck = Duck("Donald")
print(duck.breathe())
print(duck.swim())
print(duck.run())
print(duck.quack())


# 3. MULTILEVEL INHERITANCE
# A chain of inheritance: Grandparent -> Parent -> Child

class Mammal(Animal):
    def feed_young(self):
        return f"{self.name} feeds its young with milk."


class Cat(Mammal):
    def purr(self):
        return f"{self.name} says: Purrrr..."


cat = Cat("Whiskers")
print(cat.breathe())
print(cat.feed_young())
print(cat.purr())


# 4. HIERARCHICAL INHERITANCE
# Multiple child classes inherit from the same parent class.

class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying high!"

    def chirp(self):
        return f"{self.name} says: Tweet! Tweet!"


sparrow = Bird("Sparrow")
cat2    = Cat("Kitty")
dog2    = Dog("Buddy")

for animal in [sparrow, cat2, dog2]:
    print(animal.eat())

print(sparrow.fly())
print(cat2.purr())
print(dog2.bark())


# 5. HYBRID INHERITANCE
# A combination of multilevel and multiple inheritance.

class Horse(Mammal):
    def gallop(self):
        return f"{self.name} gallops swiftly!"


class Donkey(Mammal):
    def bray(self):
        return f"{self.name} says: Hee-Haw!"


class Mule(Horse, Donkey):
    def carry(self):
        return f"{self.name} can carry heavy loads."


mule = Mule("Max")
print(mule.breathe())
print(mule.feed_young())
print(mule.gallop())
print(mule.bray())
print(mule.carry())
