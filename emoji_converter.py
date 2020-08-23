message = input(">")

words = message.split(" ")
#dictionary to store emojis
emojis = {
    ":)": "😃",
    ":(":"😣"
}
output = ''
for word in words:
    output += emojis.get(word, word)+" "
print(output)
