
# print smileys
import emoji

inputs = input("> ")
words = inputs.split(" ")

#Windows + ;
emojis = {
    ":)" : "😊",
    ":(": "😢"
}

output = ""
for word in words:
    output += emojis.get(word,word) + " "

print(output)



