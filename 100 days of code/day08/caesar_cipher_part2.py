alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



# def encrypt(original_text, shift_amount):
#     encrypted_word = ""
#     for l in original_text:
#            position = alphabet.index(l) + shift_amount
#            position  = position % len(alphabet)
#            encrypted_word = encrypted_word + alphabet[position]
#     print(f"Here is the encoded result: {encrypted_word}")
#     return encrypted_word

#encrypted_word = encrypt(original_text = text, shift_amount = shift)

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.


# def decrypt(original_text, shift_amount):
#     dencrypted_word = ""
#     for l in original_text:
#            position = alphabet.index(l) - shift_amount
#            position  = position % len(alphabet)
#            dencrypted_word = dencrypted_word + alphabet[position]
#     print(f"Here is the dencoded result: {dencrypted_word}")


#decrypt(original_text = encrypted_word, shift_amount = shift)


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.


# def caesar(encode_or_decode, original_text, shift_amount):
#     if direction.lower() == 'encode':
#         encrypt(original_text = text, shift_amount = shift)
#     if direction.lower() == 'decode':
#         decrypt(original_text = text, shift_amount = shift)

        
# caesar(encode_or_decode = direction, original_text = text, shift_amount = shift)


# simpler version:
def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""
    for l in original_text:
        if encode_or_decode == 'decode':
            shift_amount = shift_amount * (-1)
                       
        position = alphabet.index(l) + shift_amount
        position  = position % len(alphabet)
        output_text = output_text + alphabet[position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    
caesar(encode_or_decode = direction, original_text = text, shift_amount = shift)


