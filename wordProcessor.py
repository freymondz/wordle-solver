from json import load, dump


def load_words():
    with open('data/words_dictionary.json') as json_file:
        data = load(json_file)
    words = data.keys()
    words_json = {}
    for word in words:
        if len(word) == 5:
            words_json[word] = 1
    with open('wordFile', 'w') as wordFile:
        dump(words_json, wordFile)


if __name__ == '__main__':
    english_words = load_words()
