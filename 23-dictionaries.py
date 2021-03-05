customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True,
}

print(customer)

print(customer["name"])

# print(customer["Name"])  # Error - No Name Key

print(customer.get("birthdate", "Jan 1 1980"))

customer["name"] = "Jack Smith"

customer["birthdate"] = "01/01/1980"
print(customer)


# Exercise
digits = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phone = str(input("Enter your Phone Number: "))
output = ""

for char in phone:
    output += digits.get(char, "#") + " "

print(output)
    
