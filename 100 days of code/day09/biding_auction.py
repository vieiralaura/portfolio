### Functionality
# - Each person writes their name and bid.
# - The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
# - Each person's name and bid are saved to a dictionary.
# - Once all participants have placed their bid, the program works out who has the highest bid and prints it.

import art

print(art.logo)


biding = {}
max_value= 0
winner = "" 


new_bids = True
while new_bids == True:
    name = input("What is your name? ")
    price = int(input("How much do you want to bid? $"))
    biding[name] = price
    if price > max_value:
        max_value = price
        winner = name
     
    
    new_bids = input("Is there anyone else who wants to bid? Yes or No\n")
        
    if new_bids.lower() == "yes" or new_bids.lower() == "y":
        new_bids = True
        print("\n"*100)
    else:
        new_bids = False
        

print(f"The winner is {winner} with a bid of ${price}")


