import json

def guess_words():
  with open('wordFile.json') as json_file:
    data = json.load(json_file)
  words = data.keys()

  print("Enter Q to quit")

  while True:

    print("Guess: ", end='')
    userInput = input()

    if userInput == 'Q' or userInput == 'q':
      break

    userInput = list(userInput)
    potential_words = list()

    for word in words:
      current_word = list(word)
      if is_valid(userInput, current_word):
        potential_words.append(''.join(current_word))

    print_words(potential_words)


def is_valid(userInput:list, current_word:list):
  is_valid_current_word = current_word.copy()
  for i in range(5): 
    if userInput[i] != is_valid_current_word[i]:
      is_valid_current_word[i] = '-'
  return userInput == is_valid_current_word


def print_words(potential_words):
  for word in potential_words:
        print(word)

        
if __name__ == '__main__':
  guess_words()