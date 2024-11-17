# Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if
#the number in he input area is odd or even.
# If it's odd print out the word "Odd" otherwise printout "Even".

# The modulo operator gives you the remainder of a division.

#asks for input
number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")