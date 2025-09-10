# Emoji Converter
message = input("-> ")
words = message.split(" ")
print(words)
emojis = {
    ":)": "😀",
    "XD": "😂",
    "<3": "❤️",
    ":3": "😍",
    ":(": "😢"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
