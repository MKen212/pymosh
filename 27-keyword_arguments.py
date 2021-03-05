def greet_user(first_name, last_name="Missing"):
    print(f"Hi there, {first_name} {last_name}!")
    print("Welcome aboard")


print("<Start>")
greet_user(last_name="Smith", first_name="John")
print("<Finish>")

def price_calc(price, shipping, discount):
    total = (price + shipping) - discount
    print(f"Total Due: {total}")

price_calc(price=10.00, shipping=1.50, discount=2.20)

# greet_user(first_name="John", "Smith")  ## Gives Error
greet_user("John", last_name="Smith")

greet_user("John")