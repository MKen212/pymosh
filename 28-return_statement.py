def square(number):
    return number * number

result = square(3)

print(result)

print(square(4))

def square_no_return(number):
    print (number * number)


print(square_no_return(4))  # Prints the result and also None


# Reusable Function
def emoji_converter(message):
    emojis = {
        ":)": "😀",
        ":(": "☹️",
    }

    words = message.split(" ")
    output = ""

    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = str(input("> "))
print(emoji_converter(message))
