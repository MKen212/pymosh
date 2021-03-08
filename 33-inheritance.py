class Mammal:
    x = 10

    def walk(self):
        print("Walking")


# class Dog:
#     def walk(self):
#         print("Walking")

# class Cat:
#     def walk(self):
#         print("Walking")


class Dog(Mammal):
    def bark(self):
        print("Woof, woof!")

class Cat(Mammal):
    pass  # Just used here as Python does not like empty classes. Pass just passes...


rover = Dog()
print(rover.x)
rover.bark()

fluffy = Cat()
fluffy.walk()


