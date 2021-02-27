i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")


# Guessing Game
secret_number = 9
guess_max = 3
guess_count = 0

while guess_count < guess_max:
    guess = int(input("Guess number (1-9): "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations - You Win!")
        break
else:
    print("Sorry - You Lose!")
