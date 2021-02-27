is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm clothes.")
else:
    print("It's lovely day.")

print("Enjoy your day!")

# Exercise
house_price = 1000000
has_credit_good = True

if has_credit_good:
    down_payment = round(house_price * 0.1)
else:
    down_payment = round(house_price * 0.2)

print(f"Amount of down payment is: ${down_payment}")