# ### Write a Pizza Delivery Program

# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill. Use the `input()` function to get a user's preferences and then 
#add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").capitalize()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").capitalize()
extra_cheese = input("Do you want extra cheese? Y or N: ").capitalize()

price = 0
if size == 'S':
    price = price + 15
elif size == 'M':
    price = price + 20
elif size == 'L':
    price = price + 25
else:
    print("Wrong size, please try again")
    
if pepperoni == 'Y':
    if size == 'S':
        price = price + 2
    else: 
        price = price +3 
elif pepperoni == 'N':
    price = price
else:
    print("Wrong option, please try again")    
    
if extra_cheese == 'Y':
    price = price + 1
elif extra_cheese == 'N':
    price = price
else:
    print("Wrong option, please try again") 
    
print(f"Your final bill is: ${price}")
    

