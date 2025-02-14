import requests
response = requests.get('https://random-word-api.herokuapp.com/word')
word = response.json()[0]
print(word)

placeholder = ""
incorrect_guesses = 0
correct_guesses= 0

for letter in word:
    placeholder += "_" 
print(placeholder)

import re

while bool(word) == 1:
    guess = input("Enter a letter:\n")
    for letter in word:
        trial = word.find(guess)
        if trial < 0:
            incorrect_guesses += 1
        else:
            positions = [match.start() for match in re.finditer(guess, word)]
            placeholder_list = list(placeholder)
            for entry in positions:
                placeholder_list[entry] = word[entry]
            placeholder = ''.join(placeholder_list)

        correct_guesses += 1
        
    for char in placeholder:
        print(char, end="")
    print()

    # if correct_guesses == len(word) - 1: #blimey
    if placeholder == word :
        print("Game over. You win!")
        break
        
    if incorrect_guesses == 8:
        print("Game over. You lose!")
        break
