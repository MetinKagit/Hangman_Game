import random
import string
import stages
import logo

WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


def create_display(secret_word):
    display_secret_word = []
    for _ in range(len(secret_word)):
        display_secret_word.append('_')
    return display_secret_word

def run_game(game_over,life):

    while not game_over:
        word_exist = False
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print("You already guess {guess}")
            continue
        if len(guess) > 1:
            print("Please enter a single character!")
            continue

        for position in range(word_legth):
            letter = secret_word[position]
            if letter == guess:
                display[position] = letter
                word_exist = True
        if word_exist is True:
            print(stages.stages[life])

        if word_exist is False:
            life -= 1
            print(stages.stages[life])
            if life == 0:
                print(stages.stages[life])
                game_over = True
                print(logo.lose)
                print("The secret word is: " + secret_word)
                exit()

        print(display)

        if '_' not in display:
            game_over = True
            print(logo.win)
            exit()

if __name__ == '__main__':

    secret_word = choose_word(wordlist)
    word_legth = len(secret_word)
    display = create_display(secret_word)
    game_over = False
    life = 6
    print(logo.logo)
    print(stages.stages[life])
    print(display)

    run_game(game_over, life)

