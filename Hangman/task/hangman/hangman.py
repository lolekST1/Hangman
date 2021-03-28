import random 
# Write your code
def game():
    word = random.choice(['python', 'java', 'kotlin', 'javascript'])
    short = ("-" * len(word))
    short_list = [a for a in short]
    tries = 8
    guesses = []
    print('H A N G M A N')
    while tries > 0:
        print('\n'+''.join([str(a) for a in short_list]))
        guess = input("Input a letter:")
        index = 0
        if len(guess) != 1:
            print("You should input a single letter")
        elif not guess.islower():
            print("Please enter a lowercase English letter")
        elif guess in guesses:
            print("You've already guessed this letter")
        elif guess not in word:
            print("That letter doesn't appear in the word")
            tries -= 1
        elif guess in short_list:
            print("No improvements")
            tries -= 1
        else:
            for letter in word:
                if letter == guess:
                    short_list[index] = letter
                index += 1
        if "-" not in short_list:
            print('''You guessed the word!
    You survived!''')
            break
        guesses.append(guess)
    else:
        print("You lost!\n")

answer = ""
while True:
    answer = input('Type "play" to play the game, "exit" to quit:')
    if answer == "play":
        game()
    if answer == "exit":
        break
