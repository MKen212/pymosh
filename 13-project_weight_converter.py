# Weight Converter Project
weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
conversion = 0.45

if unit.upper() == "L":
    result = weight * conversion
    resultString = str(result) + " kilograms"

elif unit.upper() == "K":
    result = weight / conversion
    resultString = str(result) + " pounds"
else:
    result = 0

if result == 0:
    print("Error in input!")
else:
    print(f"You are {resultString}")