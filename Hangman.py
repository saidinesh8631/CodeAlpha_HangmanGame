import os
import sys
import random
import unicodedata

# Ensure UTF-8 encoding support on Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Enable ANSI escape sequence processing on Windows
if sys.platform == "win32":
    os.system("")

# ANSI Color & Style Codes
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    
    # Foreground colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

def get_char_width(c):
    """Calculates visual column width of a character (accounting for wide emojis)."""
    if unicodedata.east_asian_width(c) in ('W', 'F'):
        return 2
    if 0x1F300 <= ord(c) <= 0x1F9FF or 0x2600 <= ord(c) <= 0x27BF:
        return 2
    return 1

def visual_width(text):
    """Returns total visual display column width of a string in terminal."""
    return sum(get_char_width(c) for c in text)

def draw_box(lines, color="", inner_width=63):
    """Draws a perfectly aligned border box around given lines with dynamic padding."""
    top = f"{color}{Color.BOLD}╔{'═' * inner_width}╗{Color.RESET}"
    bottom = f"{color}{Color.BOLD}╚{'═' * inner_width}╝{Color.RESET}"
    content = []
    for line in lines:
        vw = visual_width(line)
        pad = max(0, inner_width - vw)
        lp = " " * (pad // 2)
        rp = " " * (pad - (pad // 2))
        content.append(f"{color}{Color.BOLD}║{Color.RESET}{lp}{color}{Color.BOLD}{line}{Color.RESET}{rp}{color}{Color.BOLD}║{Color.RESET}")
    return "\n" + "\n".join([top] + content + [bottom])

def print_banner():
    """Prints a colorful retro arcade banner."""
    print(draw_box([
        " HANGMAN GAME ",
        "Guess the secret word before time runs out!"
    ], Color.CYAN))

def display_word(secret_word, guessed_letters):
    """Formats and colors the secret word with revealed and hidden letters."""
    formatted = []
    for letter in secret_word:
        if letter in guessed_letters:
            formatted.append(f"{Color.GREEN}{Color.BOLD}{letter.upper()}{Color.RESET}")
        else:
            formatted.append(f"{Color.CYAN}_{Color.RESET}")
    return "  ".join(formatted)

def render_hearts(lives_left, total_lives=6):
    """Returns visual heart indicators for player lives."""
    active_hearts = f"{Color.RED}❤ {Color.RESET}" * lives_left
    lost_hearts = f"{Color.DIM}🖤 {Color.RESET}" * (total_lives - lives_left)
    return active_hearts + lost_hearts

def format_guessed_letters(guessed_letters, secret_word):
    """Colorizes guessed letters: Green if correct, Red if wrong."""
    if not guessed_letters:
        return f"{Color.DIM}None{Color.RESET}"
    
    parts = []
    for letter in sorted(guessed_letters):
        if letter in secret_word:
            parts.append(f"{Color.GREEN}{letter.upper()}{Color.RESET}")
        else:
            parts.append(f"{Color.RED}{letter.upper()}{Color.RESET}")
    return ", ".join(parts)

def play_game():
    # 1. Predefined list of 5 words (Task 1 specification)
    words = ["python", "codealpha", "developer", "program", "script"]
    
    # 2. Random selection of word
    secret_word = random.choice(words)
    guessed_letters = set()
    max_lives = 6
    incorrect_guesses = 0
    feedback_msg = f"{Color.CYAN}✨ Game started! Enter your first guess below.{Color.RESET}"

    while incorrect_guesses < max_lives:
        lives_left = max_lives - incorrect_guesses
        
        # Display current status and stats
        print("\n" + "=" * 65)
        print(f"  {Color.BOLD}Lives:{Color.RESET}   {render_hearts(lives_left, max_lives)} ({lives_left}/{max_lives})")
        print(f"  {Color.BOLD}Guessed:{Color.RESET} {format_guessed_letters(guessed_letters, secret_word)}")
        print("\n  " + f"{Color.BOLD}Word:{Color.RESET}    " + display_word(secret_word, guessed_letters))
        print("=" * 65)
        
        if feedback_msg:
            print(f"\n{feedback_msg}\n")
            feedback_msg = ""

        # Player input
        try:
            raw_input = input(f"{Color.YELLOW}{Color.BOLD}👉 Enter a letter: {Color.RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Color.YELLOW}Game exited. See you next time!{Color.RESET}")
            return

        guess = raw_input.strip().lower()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            feedback_msg = f"{Color.YELLOW}⚠️  Invalid input! Please enter a single letter (a-z).{Color.RESET}"
            continue

        if guess in guessed_letters:
            feedback_msg = f"{Color.YELLOW}⚠️  You already guessed '{guess.upper()}'! Try a different letter.{Color.RESET}"
            continue

        guessed_letters.add(guess)

        # Check guess
        if guess in secret_word:
            feedback_msg = f"{Color.GREEN}{Color.BOLD}✅ Spot on! '{guess.upper()}' is in the word!{Color.RESET}"
            
            # Check Win condition
            if all(letter in guessed_letters for letter in secret_word):
                print("\n" + "=" * 65)
                print("\n  " + f"{Color.BOLD}Word:{Color.RESET}    " + display_word(secret_word, guessed_letters))
                print("=" * 65)
                print(draw_box([
                    "🎉 🏆  CONGRATULATIONS! YOU WON!  🏆 🎉",
                    "You successfully revealed the secret word:",
                    f"'{secret_word.upper()}'"
                ], Color.GREEN))
                return
        else:
            incorrect_guesses += 1
            feedback_msg = f"{Color.RED}{Color.BOLD}❌ Bummer! '{guess.upper()}' is NOT in the word.{Color.RESET}"

    # Loss condition (incorrect_guesses reached max_lives)
    print("\n" + "=" * 65)
    print(f"  {Color.BOLD}Lives:{Color.RESET}   {render_hearts(0, max_lives)} (0/{max_lives})")
    print("=" * 65)
    print(draw_box([
        "💀  GAME OVER! YOU LOST!  💀",
        "You ran out of attempts!",
        f"The secret word was: '{secret_word.upper()}'"
    ], Color.RED))

def main():
    print_banner()
    while True:
        play_game()
        try:
            choice = input(f"\n{Color.CYAN}🔁 Would you like to play again? (y/n): {Color.RESET}").strip().lower()
            if choice not in ('y', 'yes'):
                print(f"\n{Color.GREEN}Thanks for playing Hangman! GAME Goodbye! 👋{Color.RESET}\n")
                break
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Color.GREEN}Goodbye! 👋{Color.RESET}\n")
            break

if __name__ == "__main__":
    main()
