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
        user_input = input()

        if user_input == 'Q' or user_input == 'q':
            break
        elif user_input == "G":
            guess(words)
        elif user_input == "R":
            remove(words)


def guess(words):
    print("Guess: ", end='')
    user_guess = list(input())
    potential_words = list()

    if len(user_guess) != 5:
        print("Guess needs to be a 5 letter word")
        return

    for word in words:
        current_word = list(word)
        if is_valid(user_guess, current_word):
            potential_words.append(word)

    print_words(potential_words)


def remove(words: list):
    print("Remove: ", end='')
    user_remove = list(input())
    remove_words = words.copy()

    for word in remove_words:
        current_word = list(word)
        if is_valid(user_remove, current_word):
            words.remove(word)


def is_valid(user_input: list, current_word: list):
    is_valid_current_word = current_word.copy()

    for i in range(5):
        if user_input[i] != is_valid_current_word[i]:
            is_valid_current_word[i] = '-'

    return user_input == is_valid_current_word


def print_words(potential_words):
    if not potential_words:
        print("No valid words")
    else:
        print(" Possible Words:")
        for word in potential_words:
            print("  " + word)


if __name__ == '__main__':
    guess_words()
