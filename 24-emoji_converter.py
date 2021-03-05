emojis = {
    ":)": "😀",
    ":(": "☹️"
}

message = str(input("> "))
words = message.split(" ")
output = ""

for word in words:
    output += emojis.get(word, word) + " "

print(output)
