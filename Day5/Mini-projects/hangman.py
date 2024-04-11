import random


def choose_word():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
                 'credit card', 'rush', 'south']
    return random.choice(wordslist)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display


def display_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
          ---
        """
    ]
    print(stages[attempts])


def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect!")
            attempts -= 1
            display_hangman(attempts)
            print("Attempts left:", attempts)

        print("Word:", display_word(word, guessed_letters))

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)


hangman()