from json import load


def guess_words():
    with open('data/wordFile.json') as json_file:
        data: dict = load(json_file)
    words = list(data.keys())
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
            words = remove(words)


def guess(words: list):
    print()
    print("Guess: ", end='')
    user_guess = list(input())
    potential_words = list()

    if len(user_guess) != 5:
        print("Your guess needs to be a 5 letter word")
        return

    for word in words:
        if is_valid(user_guess, list(word)):
            potential_words.append(word)

    print_words(potential_words)


def remove(words: list):
    print()
    print("Remove: ", end='')
    user_remove = list(input())
    remove_words = words.copy()

    for word in remove_words:
        if is_valid(user_remove, list(word)):
            remove_words.remove(word)

    return remove_words


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
