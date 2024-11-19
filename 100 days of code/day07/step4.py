stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



# ### TODO-1: 
# - Create a variable called `lives` to keep track of the number of lives left.
# - Set `lives` to equal `6`.


# ### TODO-2: 
# - If `guess` is not a letter in the `chosen_word`, Then reduce `lives` by `1`. 
# - If `lives` goes down to `0` then the game should end, and it should print "You lose."

# <div class="hint">
#   The not in keywords will be your friend in this todo. You can check if something exists in the chosen_word completely separately from the rest of the code.
# </div>


# ### TODO-3: 
# - print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.





import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder =  ""
for l in chosen_word:
    placeholder = placeholder + "_ "
print(placeholder)

game_over = False
letters_guessed = []
lives = 6
print(stages[lives])

while not game_over:

    guess = input("Please guess a letter: ").lower()
    
    display = ""

    if guess not in chosen_word:
        lives = lives -1
        

        
    for l in chosen_word:
        if l == guess:
            display = display + l
            letters_guessed.append(l)

        elif l in letters_guessed:
            display = display + l
    
        else:
            display = display + "_ "
            
    print(display)
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You've won!")
    elif lives == 0:
        game_over = True
        print("No more lives. You've lost!")

