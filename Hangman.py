import random

def display_word(secret_word, guessed_letters):
    """Returns the current state of the word with guessed letters revealed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def main():
    # 1. Predefined list of 5 words
    words = ["python", "codealpha", "developer", "program", "script"]
    
    # 2. Randomly select a word from the list
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts_left = 6
    
    print("=" * 45)
    print("      WELCOME TO CODEALPHA HANGMAN GAME      ")
    print("=" * 45)
    print("Guess the secret word one letter at a time!\n")

    # 3. Main game loop
    while attempts_left > 0:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Attempts remaining: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
            # Check for win condition
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\n🎉 Congratulations! You guessed the word: '{secret_word}'!")
                break
        else:
            attempts_left -= 1
            print(f"❌ Incorrect! '{guess}' is not in the word.")

    if attempts_left == 0:
        print(f"\n💀 Game Over! The secret word was: '{secret_word}'")

if __name__ == "__main__":
    main()
