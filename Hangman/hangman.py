import random

print("Welcome to hangman game!")
print('''
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

''')

words = 'ant baboon bat bear camel cat cobra cougar coyote crow deer dog donkey duck eagle fox frog goat goose hawk ' \
        'lion lizard monkey moose mouse mule owl panda parrot pigeon python rabbit rat raven rhino seal shark sheep ' \
        'snake spider swan tiger turkey turtle whale wolf zebra'.split()

# Choosing random word from word list
random_word = random.choice(words)

# Lists to print the blanks and letter
blanks = []
letters = []

# Giving 6 lives to spend player
lives_left = 6

# Creating blanks to print
for i in range(len(random_word)):
    blanks.append("_")
    letters.append(random_word[i])

# Boolean values for indication of status
game_over = False
game_won = False


# Print the word with blanks
def print_word(blanks_):
    for a in blanks_:
        print(a, end=" ")
    print()
    print()

# Printing the ascii model of hangman
def print_ascii_hangman(lives_left_):
    if lives_left_ == 6:
        print(" +---+")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("========")
    elif lives_left_ == 5:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("     |")
        print("========")
    elif lives_left_ == 4:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("     |")
        print("========")
    elif lives_left_ == 3:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("     |")
        print("========")
    elif lives_left_ == 2:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("     |")
        print("========")
    elif lives_left_ == 1:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("     |")
        print("========")
    elif lives_left_ == 0:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("     |")
        print("========")


#Game starts
while not game_over:
    print_ascii_hangman(lives_left)
    print_word(blanks)
    print(f"Lives left: {lives_left}")
    letter_guessed = input("Guess a letter: ")
    if random_word.__contains__(letter_guessed):
        for j in range(len(letters)):
            if letter_guessed == letters[j]:
                blanks[j] = letter_guessed
    else:
        lives_left -= 1

    if lives_left == 0:
        print_ascii_hangman(lives_left)
        print(f"It was {random_word.upper()}")
        print("GAME OVER")
        game_over = True

    game_won = True
    for blank in blanks:
        if blank == "_":
            game_won = False

    if not game_won:
        continue
    print_word(blanks)
    print("CONGRATS")
    game_over = True

print()
input("Press Enter to continue...")
