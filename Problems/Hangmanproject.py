import random

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

print("Welcome to Hangman!")

# taking a random word from the list
my_list = ["quidditch", "hobbyhorsing", "lacrosse", "curling", "softball", "gymnastics", "racewalking"]

# first way
random.shuffle(my_list)
my_word = my_list.pop()

# tracks number of misses
incorrect_guesses = 0
level = 0
word_letters = []
guessed_letters = []
done = False
for i in range(len(my_word)):
    print("_ ", end="")

while not done:
    print(gallows[level])
    correct_guesses = 0
    letters_remaining = len(my_word)
    guess = input("\nPick a letter: ")
    if guess.lower() in guessed_letters:
        print("You already guessed that. Pick another letter.")
    if guess.lower() not in guessed_letters:
        guessed_letters.append(guess)
    if guess.lower() in my_word.lower():
        if guess.lower() not in guessed_letters:
            correct_guesses += 1
        word_letters.append(guess.lower())
    else:
        incorrect_guesses += 1
        level += 1
    for letter in my_word.lower():
        if letter in word_letters:
            print(letter + " ", end="")
            letters_remaining -= 1
        else:
            print("__", end=" ")

    if incorrect_guesses >= 6:
        print("You lose. Want to try again?")
        done = True

    if letters_remaining == 0:
        done = True
        print("You win! Want to try again?")











