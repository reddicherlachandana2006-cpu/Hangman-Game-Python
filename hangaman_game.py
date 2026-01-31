import random
words = ["python", "coding", "hangman", "program", "computer"]
word = random.choice(words)
guessed_letters = []
attempts = 6
print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_"
    print("\n Word:", display_word)
    print("Remaining attempts:",attempts)
    if "_" not in display_word:
        print("Congratulations! You guessed the word correctly!")
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess not in word:
        print("Wrong guess!")
        attempts -= 1
    else:
        print("Correct guess!")
if attempts == 0:
    print("\n Game Over! The word was:", word)