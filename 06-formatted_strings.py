first_name = "John"
last_name = "Smith"
message = first_name + " [" + last_name + "] is a coder."
print(message)

# best option
msg1 = f"{first_name} [{last_name}] is a coder."
print(msg1)

# alternate but more complex to understand what goes where
msg2 = "{} [{}] is a coder."
print(msg2.format(first_name, last_name))