for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")


# Challenge exercise
numbers = [5, 2, 5, 2, 2]

for row_count in numbers:
    output = ""
    for item in range(row_count):
        output += "x"
    print(output)

print()

# Challenge 2
numbers2 = [2, 2, 2, 2, 5]

for row_count in numbers2:
    output = ""
    for item in range(row_count):
        output += "x"
    print(output)
