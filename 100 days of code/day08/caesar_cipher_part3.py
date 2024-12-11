# TODO-1: Import and print the logo from art.py when the program starts.


import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

    ### TODO-2: 
    #What happens if the user enters a number/symbol/space that's not in the List `alphabet`?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    
    
def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""
    if encode_or_decode == 'decode':
        shift_amount = shift_amount * (-1)
    for l in original_text:
        if l in alphabet:
            position = alphabet.index(l) + shift_amount
            position  = position % len(alphabet)
            output_text = output_text + alphabet[position]
        else:
            output_text = output_text + l
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar(encode_or_decode = direction, original_text = text, shift_amount = shift)

# TODO-3: Can you figure out a way to restart the cipher program?
# `Type 'yes' if you want to go again. Otherwise, type 'no'.`
# If they type 'yes' then ask them for the direction/text/shift again and call the `caesar()` function again.

# Try creating a while loop that continues to execute the program if the user types 'yes'.


again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")

while again.lower() == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(encode_or_decode = direction, original_text = text, shift_amount = shift)
    again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")

    







