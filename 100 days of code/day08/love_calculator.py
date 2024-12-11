# Love Calculator
# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out. 

# Love Calculator

def calculate_love_score(name1, name2):
    names = name1.lower() +name2.lower()
    true_occurs = 0
    love_occurs = 0
    for l in names:
        if l in "true":
            true_occurs = true_occurs + 1
        if l in "love":
            love_occurs = love_occurs +1
    love_score = str(true_occurs) + str(love_occurs)
    print(love_score)
             
    
calculate_love_score("laura vieira", "will smith")

calculate_love_score("laura ferreira de bello vieira", "philip sampaio silva")

