temperature = 35

if temperature == 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")


# Exercise
name = input("Enter name: ")

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 20:
    print("Name must be a maximum of 20 characters.")
else:
    print("Name looks good!")
