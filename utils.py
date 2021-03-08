# File with functions to be included into the main file - Used with 34-modules.py

def find_max(numbers):
    maximum = numbers[0]
    for value in numbers:
        if value > maximum:
            maximum = value
    return maximum

