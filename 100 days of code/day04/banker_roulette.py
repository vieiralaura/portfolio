## Banker roulette
#Figure out how to pick a random name from the list of rich friends that like doing a 'banker roulette', randomly deciding who will pay the bill.

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random
random_rich = random.randint(0,4)

print(friends[random_rich])


##second option
print(random.choice(friends))