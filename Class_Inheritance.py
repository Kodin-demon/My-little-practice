
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Dog(Animal):
    def speak(self):
        print("Bark baRk bArk")

class Lizard(Animal):
    def hissing(self):
        print("Hiss")

cat = Cat("Lucky")
dog = Dog("Shaggy")
lizard = Lizard("MstKid")

print(lizard.name)
print(lizard.is_alive)
lizard.eat()
lizard.drink()
lizard.sleep()
dog.speak()
cat.speak()
lizard.hissing()


