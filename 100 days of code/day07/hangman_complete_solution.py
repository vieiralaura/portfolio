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

