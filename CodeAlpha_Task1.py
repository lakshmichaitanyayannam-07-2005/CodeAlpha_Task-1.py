import random

words = ["python", "apple", "computer", "coding", "hangman"]

word = random.choice(words)
guessed = []
attempts = 6

print("🎮 Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You Won!")
        print("The word is:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Remaining Attempts:", attempts)

if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)
