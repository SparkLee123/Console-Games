import random as rd

answers = ['apple', 'banana', 'carrot', 'durian', 'egg', 'fish', 'grape']

print("Welcome to Hangman!")

word = rd.choice(answers)
lword = word.lower()
letters = ['_'] * len(word)
for z in range(len(letters)):
    if word[z] == ' ':
        letters[z] = ' '
lives = 6

pg = []

while True:
    print(' '.join(letters))
    print("Lives left:", lives)
    print("Previous guesses:", ', '.join(pg))
    while True:
        guess = input('Enter a letter: ')
        guess = guess.lower()
        if len(guess) > 1 or guess.isdigit():
            print("INVALID INPUT")
            continue
        elif guess in pg:
            print("LETTER HAS ALREADY BEEN USED")
            continue
        else:
            break
    if guess in lword:
        for x in range(len(letters)):
            if lword[x] == guess:
                letters[x] = guess
    else:
        print("Not there!")
        lives -= 1
    pg.append(guess)
    if lives == 0:
        print("You lose! The answer was:", word)
        while True:
            pa = input("Play Again? (Y/N) ")
            if pa == "Y":
                word = rd.choice(answers)
                lword = word.lower()
                letters = ['_'] * len(word)
                lives = 6
                pg = []
                break
            elif pa == "N":
                break
            else:
                print("INVALID INPUT")
        if pa == "N":
            break
    if ''.join(letters) == lword:
        print(' '.join(letters))
        print(f"You win! You had {lives} lives left.")
        while True:
            pa = input("Play Again? (Y/N) ")
            if pa == "Y":
                word = rd.choice(answers)
                lword = word.lower()
                letters = ['_'] * len(word)
                lives = 6
                pg = []
                break
            elif pa == "N":
                break
            else:
                print("INVALID INPUT")
        if pa == "N":
            break