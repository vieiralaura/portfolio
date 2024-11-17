#welcome message for the user
print("Welcome to the tip calculator!")
#ask for the total bill input as save it in a variable "total"
total = float(input("What was the total bill?$"))
#ask for the percent tip input as save it in a variable "percent"
percent = int(input("How much tip would you like to give?10, 12 or 15?"))
#ask for the number of people to split the bill input as save it in a variable "people"
people = int(input("How many people to split the bill?"))
#calculate the tip
tip = (total + total*percent/100)/people
#print the tip for each people
print(f"Each person should pay: ${tip}")