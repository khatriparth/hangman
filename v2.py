import re

import requests
response = requests.get('https://random-word-api.herokuapp.com/word')
word = response.json()[0]
# print(word)


title = "HANGMAN"
placeholder = ""
incorrect_guesses = 0
correct_guesses= 0
used_guesses = ""

alphabets = [
    [' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['  ', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['   ', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
]

print(title)

for letter in word:
    placeholder += "_"
print(placeholder)

print("Available letters:")
for unit in alphabets:
    print(*unit, sep=" ")

while bool(word) == 1:
    guess = input("Guess a letter:\n").lower()
    if guess in used_guesses:
        print("You have already guessed this letter. Try again")
    elif len(guess) != 1:
        print("Please enter only one letter at a time.")
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter a valid letter.")
    elif guess == "":
        print("Please enter a letter.")
    else:
        used_guesses += guess
        trial = word.find(guess)
        if trial < 0:
            incorrect_guesses +=1
        else:
            correct_guesses += 1
            for letter in word:
                positions = [match.start() for match in re.finditer(guess, word)]
                placeholder_list = list(placeholder)
                for entry in positions:
                    placeholder_list[entry] = word[entry]
                placeholder = ''.join(placeholder_list)
                
                
                
           
                
                
            
        print(title)
        
        for char in placeholder:
            print(char, end="")
        print("\n")
    
        # print("Incorrect guesses:", incorrect_guesses, end=". ")
        print("Lives:", 7 - incorrect_guesses)
    
        for letter in used_guesses:
            for i in range(len(alphabets)):
                if letter in alphabets[i]:
                    j = alphabets[i].index(letter)
                    alphabets[i][j] = " "
        print("Available letters:")
        for unit in alphabets:
            print(*unit, sep=" ")
        
    # if correct_guesses == len(word) - 1: #blimey
    if placeholder == word :
        print("-----------------------------------------------------")
        print("Game over. You won!")
        print("-----------------------------------------------------")
        print("Guesses:-\n Correct:", correct_guesses, "Incorrect:", incorrect_guesses)
        print("-----------------------------------------------------")
        break
        
    if incorrect_guesses == 7:
        print("-----------------------------------------------------")
        print("Game over. You lost!")
        print("-----------------------------------------------------")
        print("The word was: ", word)
        print("-----------------------------------------------------")
        print("Better luck next time!")
        print("-----------------------------------------------------")
        break