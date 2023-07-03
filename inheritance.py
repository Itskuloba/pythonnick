class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplementedError("Child classes must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Horse(Animal):
    def speak(self):
        return "Neighs"


dog = Dog("Bosco", "White")
print(dog.name)
print(dog.color)
print(dog.speak())

cat = Cat("Tom", "Black")
print(cat.name)
print(cat.color)
print(cat.speak())

horse = Horse("Sally", "Brown")
print(horse.name)
print(horse.color)
print(horse.speak())
