print("Welcome to the tip calculator!")
total = float(input("What was the total bill?$"))
percent = int(input("How much tip would you like to give?10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
tip = (total + total*percent/100)/people
print(f"Each person should pay: ${tip}")