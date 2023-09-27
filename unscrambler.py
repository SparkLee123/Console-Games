import random as rd
def get_league_of_legends_champions():
  GAME_VERSION = '13.17.1' # Change this game version if you want another version's list of champions

  # DO NOT MODIFY ANYTHING IN THIS FUNCTION BELOW THIS LINE
  import requests
  d = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{GAME_VERSION}/data/en_US/champion.json')
  if d.status_code != 200:
    print('Error retrieving data')
    return []
  data = d.json()['data']
  return sorted([data[champ]['name'].upper() for champ in data])

def get_valorant_agents():
  # DO NOT MODIFY ANYTHING IN THIS FUNCTION!
  import requests
  d = requests.get('https://valorant-api.com/v1/agents?isPlayableCharacter=true')
  if d.status_code != 200:
    print('Error retrieving data')
    return []
  data = d.json()['data']
  return sorted([agent['displayName'].upper() for agent in data])

answers = get_valorant_agents() + get_league_of_legends_champions()
lives = 5
word = rd.choice(answers)
spaces = word.count(" ") + 1
spaceless = word.replace(" ", "")
scramble = rd.sample(spaceless, len(spaceless))
guesses = []
while ''.join(scramble) == word:
    scramble = rd.sample(word, len(word))
print("Welcome to the Word Unscrambler!")
print("Unscramble this:", ''.join(scramble), f"({spaces} word(s))")
def validate_input(s):
    word1 = list(s)
    if len(s) != len(word):
        return False
    for x in range(len(s)):
        if word[x] in word1:
            word1.pop(word1.index(word[x]))
            continue
        else:
            return False
    return True
while True:
    guess = input()
    guess = guess.upper()
    if guess == word:
        print("You win!")
        while True:
            again = input("Try again? Y/N: ")
            if again == "Y":
                lives = 5
                word = rd.choice(answers)
                spaces = word.count(" ") + 1
                spaceless = word.replace(" ", "")
                scramble = rd.sample(spaceless, len(spaceless))
                while ''.join(scramble) == word:
                    scramble = rd.sample(word, len(word))
                print("Unscramble this:", ''.join(scramble), f"({spaces} word(s))")
                guesses = []
                break
            elif again == "N":
                print("Thanks for playing!")
                break
            else:
                print("INVALID")
                continue
        if again == "Y":
            continue
        if again == "N":
            break
    elif validate_input(guess) == False:
        print("INVALID: not a valid anagram")
    elif guess in guesses:
        print("INVALID: guess has already been used")
    else:
        lives -= 1
        guesses.append(guess)
        if lives == 0:
            print(f"You lose! The correct answer was: {word}")
            while True:
                again = input("Try again? Y/N: ")
                if again == "Y":
                    lives = 5
                    word = rd.choice(answers)
                    spaces = word.count(" ") + 1
                    spaceless = word.replace(" ", "")
                    scramble = rd.sample(spaceless, len(spaceless))
                    while ''.join(scramble) == word:
                        scramble = rd.sample(word, len(word))
                    print("Unscramble this:", ''.join(scramble), f"({spaces} word(s))")
                    guesses = []
                    break
                elif again == "N":
                    print("Thanks for playing!")
                    break
                else:
                    print("INVALID")
                    continue
            if again == "Y":
                continue
            if again == "N":
                break
        print(f"Incorrect! {lives} lives left.")
    