import json


def guess_words():
    with open('data/wordFile.json') as json_file:
        data: dict = json.load(json_file)
    words = list(data.keys())
    # TODO: In the future I should specify if you also want to remove letters
    print('''
Welcome to my wordle-solver!
    ''')

    while True:
        print('''
(Q)uit (G)uess (R)emove
        ''')
        userInput = input()

        if userInput == 'Q' or userInput == 'q':
            break
        elif userInput == "G":
            guess(words)
        elif userInput == "R":
            remove(words)


def guess(words):
    print("Guess: ", end='')
    userGuess = list(input())
    potential_words = list()

    if len(userGuess) != 5:
        print("Guess needs to be a 5 letter word")
        return

    for word in words:
        current_word = list(word)
        if is_valid(userGuess, current_word):
            potential_words.append(word)

    print_words(potential_words)


def remove(words: list):
    print("Remove: ", end='')
    userRemove = list(input())
    remove_words = words.copy()

    for word in remove_words:
        current_word = list(word)
        if is_valid(userRemove, current_word):
            words.remove(word)


def is_valid(userInput: list, current_word: list):
    is_valid_current_word = current_word.copy()

    for i in range(5):
        if userInput[i] != is_valid_current_word[i]:
            is_valid_current_word[i] = '-'

    return userInput == is_valid_current_word


def print_words(potential_words):
    if not potential_words:
        print("No valid words")
    else:
        print(" Possible Words:")
        for word in potential_words:
            print("  " + word)


if __name__ == '__main__':
    guess_words()
