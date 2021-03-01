names = ["John", "Jack", "Sarah", "Susan"]
print(names)

print(names[2])
print(names[-1])
print(names[1:3])

names[2] = "Sandra"
print(names[1:3])


# Exercise

my_list = [3, 5, 12, 6, 1, 10]
largest_number = 0

for value in my_list:
    if value > largest_number:
        largest_number = value

print(f"Largest number: {largest_number}")