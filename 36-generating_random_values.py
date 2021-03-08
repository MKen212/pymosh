import random


for i in range(3):
    print(random.randint(10, 20))


members = [
    "John",
    "Mary",
    "Bob",
    "Mark",
]

leader = random.choice(members)
print(leader)


# Exercise
class Dice:
    def roll(self):
        value1 = random.randint(1, 6)
        value2 = random.randint(1, 6)
        return (value1, value2)


dice = Dice()
result = dice.roll()
print(f"You have rolled a '{result[0]}' and a '{result[1]}'")
