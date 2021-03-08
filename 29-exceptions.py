try: 
    age = int(input("Enter Age: "))
    income = 20000
    risk = income / age
    print(age, income, risk)
except ValueError:
    print("Error - You need to enter and integer value.")
except ZeroDivisionError:
    print("Error - You cannot use zero.")

