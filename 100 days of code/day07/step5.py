# ### TODO-1: 
# - Update the word list to use the `word_list` from hangman_words.py

# ### TODO-2: 
# - Update the code to use the `stages` from the file hangman_art.py

# ### TODO-3: 
# - Import the `logo` from hangman_art.py and print it at the start of the game.

# ### TODO-4: 
# - If the user has entered a letter they've already guessed, print the letter and let them know.
# - We should not deduct a life for this.
# - e.g. You've already guessed a

# ### TODO-5: 
# - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# - e.g. You guessed d, that's not in the word. You lose a life.

# ### TODO-6: 
# - Update the code below to tell the user how many lives they have left.
# ```print("****************************<???>/6 LIVES LEFT****************************")```

# ### TODO 7: 
# - Update the print statement to give the user the correct word they were trying to guess.
# - e.g. `IT WAS <Correct Word>! YOU LOSE`



import random
import hangman_words as hw

import hangman_art as ha

word_list = hw.word_list
stages = ha.stages
logo = ha.logo
logo_final = ha.logo_final

chosen_word = random.choice(word_list)

print(logo)

print(chosen_word)   ### APAGAR

game_over = False
letters_guessed = []
lives = 6
print(stages[lives])


placeholder =  ""
for l in chosen_word:
    placeholder = placeholder + "_ "
print(placeholder)

wrong_guessed = []
while not game_over:

    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Please guess a letter: ").lower()

    if guess in letters_guessed:
        print(f"You've already guessed {guess}, try another letter!")
        
        
    display = ""

    if guess not in chosen_word:
        lives = lives -1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        wrong_guessed.append(guess)
      
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
        print("****************You've won!****************")
        print(logo_final)
    elif lives == 0:
        game_over = True
        print(f"****************No more lives. You've lost! The word was {chosen_word} ****************")

