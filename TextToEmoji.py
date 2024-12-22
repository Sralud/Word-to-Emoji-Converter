emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "angry": "😡",
    "surprised": "😲",
    "laugh": "😂",
    "cool": "😎",
    "cry": "😭",
    "heart": "💖",
    "star": "⭐",
    "thumbsup": "👍",
    "thumbsdown": "👎",
    "peace": "✌️",
    "fire": "🔥",
    "sun": "☀️",
    "moon": "🌙",
    "coffee": "☕",
    "cake": "🍰",
    "apple": "🍎",
    "tree": "🌳",
    "earth": "🌍",
    "world": "🌎",
    "dog": "🐕",
    "cat": "🐱",
    "bird": "🐦",
    "fish": "🐟",
    "flower": "🌸",
    "car": "🚗",
    "rocket": "🚀",
    "music": "🎵",
    "camera": "📷",
    "book": "📚"
}

def emojiLetters(word):
    return ''.join(f':{char}:' for char in word)

def convertEmojitext(input_text):
    words = input_text.split()
    result = []

    for word in words:
        word_lower = word.lower()
        result.append(emoji_dict.get(word_lower, emojiLetters(word)))
    return ' '.join(result)

print("WORD TO EMOJI CONVERTER:"
      "\n-Enter a word to start"
      "\n-Enter 'exit' or 'quit' to stop\n")

while True:
    user_input = input("Enter a word: ")

    if user_input.lower() == "exit" or user_input.lower() == "quit":
        print("Thanks you!")
        break

    emoji_text = convertEmojitext(user_input)
    print("Converted Emoji: ", emoji_text)