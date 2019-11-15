def emoji_conver(input):
    words = input.split(" ")
    # Windows + ;
    emojis = {
        ":)": "😊",
        ":(": "😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_conver(message))


