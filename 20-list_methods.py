numbers = [5, 2, 1, 7, 4]
print(numbers)

numbers.append(20)
print(numbers)

numbers.insert(3, 5)
print(numbers)

numbers.remove(1)
print(numbers)

numbers.clear()
print(numbers)

numbers = [5, 2, 1, 7, 4]
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(7))

# print(numbers.index(3))  # Gives an error

print(1 in numbers)
print(3 in numbers)

numbers.insert(3, 5)
print(numbers)

print(numbers.count(5))
print(numbers.count(3))

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers1 = [5, 2, 1, 7, 4]
numbers2 = numbers1
numbers3 = numbers1.copy()

numbers1.append(20)
numbers2.append(15)
print(numbers1)
print(numbers2)
print(numbers3)
print()

# Exercise
dupe_list = [2, 2, 4, 6, 3, 4, 6, 1]
print(dupe_list)
unique_list = []

for value in dupe_list:
    if value not in unique_list:
        unique_list.append(value)

print(unique_list)
