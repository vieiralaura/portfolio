### TODO-1
# - Use a while loop to let the user guess again. 
# - The loop should only stop once the user has guessed all the letters in the chosen_word.
# - At that point `display` has no more blanks ("_"). Then you can tell the user they've won.

# <div class="hint">
#   You can use the in keyword to check if a String or List contains a particular item. 

# e.g. Google: check if a letter is present in a string python 
# </div>

# ### TODO-2
# - Update the for loop so that previous guesses are added to the `display` String.
# - At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.

# <div class="hint">
#   Think about how you can store the matched letters and use an elif to check if a letter has been matched before.
# </div>


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

while not game_over:

    guess = input("Please guess a letter: ").lower()
    
    display = ""

    
    for l in chosen_word:
        if l == guess:
            display = display + l
            letters_guessed.append(l)
        elif l in letters_guessed:
            display = display + l

        else:
            display = display + "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You've won!")
