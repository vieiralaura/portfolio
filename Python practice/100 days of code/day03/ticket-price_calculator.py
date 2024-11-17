print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

price = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))

    if age < 12:
        price = price + 5
    elif age < 18:
        price = price + 7
    elif age < 45:
        price = price + 12
    else: 
        price = 0
    print(f"Your ticket price is: ${price}")

    photo = input("Do you want to take photos? Y or N: ").capitalize()

    if photo == 'Y':
        price = price + 3
    elif photo == 'N':
        price = price
    else: 
        print("Wrong option, please try again") 
        
    print(f"Your final ticket price is: ${price}")

else:
    print("Sorry, you have to grow taller before you can ride.")
