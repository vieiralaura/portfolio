### Heads or Tails
#Create a coin flip program using what you have learnt about randomisation in Python.
#It should randomly print "Heads" or "Tails" everytime it is run. 

#You'll need to think about what you have learnt about conditional statements in Python.


import random

flip_coin = random.random()

if flip_coin < 0.5:
    print("Heads")
else:
    print("Tails")