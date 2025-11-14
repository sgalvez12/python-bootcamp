banned_words = ("moist", "break", "raise")

# TODO: Ask the user for a word
# TODO: If the word is in banned_words, say "Banned"

user_input = input("Enter a word: ")
if user_input in banned_words:
    print("Banned")
