# 🎮 Hangman Game | Python

A simple, interactive, and colorful **Hangman Game developed using Python** as part of my CodeAlpha Python Programming Internship.

The objective of this game is to guess the secret word one letter at a time. The player gets six incorrect guesses before the game ends.

## 📌 About the Project

This project is a console-based word-guessing game developed using Python. It uses basic programming concepts such as loops, conditional statements, functions, strings, sets, and random word selection.

The game also includes colorful terminal output, heart indicators for remaining lives, input validation, and an option to play again.

## ✨ Features

- 🎯 Random selection from 5 predefined words.
- ❤️ Six chances to guess the secret word.
- 🔤 Letter-by-letter word guessing.
- 🎨 Colorful terminal interface using ANSI escape codes.
- 💚 Correct guesses highlighted in green.
- ❌ Incorrect guesses highlighted in red.
- ⚠️ Input validation for invalid and repeated guesses.
- 🏆 Winning and game-over messages.
- 🔁 Option to play multiple rounds.
- 🛑 Handles keyboard interruption and end-of-input errors.

## 🛠️ Technologies Used

- **Language:** Python 3
- **IDE:** Visual Studio Code
- **Modules:** `os`, `sys`, `random`, `unicodedata`
- **Interface:** Command-line / Terminal

## 🧠 Python Concepts Used

| Concept | Purpose |
|---|---|
| Lists | Store the predefined words |
| Random module | Select a random secret word |
| Sets | Keep track of guessed letters |
| While loops | Continue the game until it ends |
| If-else statements | Check guesses and game conditions |
| Functions | Organize the code into reusable blocks |
| String methods | Process and validate user input |
| Exception handling | Handle interruptions safely |
| ANSI escape codes | Add colors and styles to the terminal |

## 📂 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py
├── README.md
└── .gitignore
```

## ⚙️ Requirements

Before running the project, make sure you have:

- Python 3 installed.
- Visual Studio Code or another Python editor.
- A terminal that supports Unicode characters and ANSI colors for the best display.

**No external Python packages are required.**

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Open the Project Folder

```bash
cd CodeAlpha_HangmanGame
```

### Step 3: Run the Program

On Windows, open the VS Code terminal and execute:

```bash
python hangman.py
```

If that command does not work, try:

```bash
py hangman.py
```

## 🎮 How to Play

1. Start the game.
2. The program randomly selects a secret word.
3. Enter one letter when prompted.
4. Correct guesses reveal the matching letters.
5. Incorrect guesses reduce your remaining lives.
6. Guess all the letters correctly to win.
7. If you make six incorrect guesses, the game ends.
8. Enter `y` to play again or `n` to exit.

## 💻 Sample Output

```text
╔═══════════════════════════════════════════════════════════════╗
║                       HANGMAN GAME                            ║
║          Guess the secret word before time runs out!          ║
╚═══════════════════════════════════════════════════════════════╝

Lives:   ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ (6/6)
Guessed: None

Word:    _ _ _ _ _ _

Enter a letter: p

Spot on! 'P' is in the word!
```

*Note: This is an illustrative example. The actual terminal output includes colors, decorative borders, and additional game information.*

## 🎯 Project Objectives

- Practice Python programming fundamentals.
- Understand lists, sets, strings, and random selection.
- Develop problem-solving and logical thinking skills.
- Learn input validation and exception handling.
- Build an interactive command-line application.
- Gain practical experience in project development and GitHub documentation.

## 🔮 Future Enhancements

The project can be improved by adding:

- Difficulty levels such as Easy, Medium, and Hard.
- Hints to help players guess words.
- Word categories such as programming, animals, and technology.
- Score tracking and winning streaks.
- A larger word database.
- Unit tests for game logic.
- A graphical user interface.

## 👨‍💻 Internship Details

- **Organization:** CodeAlpha
- **Internship Domain:** Python Programming
- **Task:** Hangman Game
- **Project Type:** Beginner-level Python console application

## 📜 License

This project is created for educational and learning purposes.

---

**Developed with Python as part of my CodeAlpha Python Programming Internship.**

Thank you for checking out my project! ⭐
