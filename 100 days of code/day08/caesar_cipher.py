import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
  
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

again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")

while again.lower() == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(encode_or_decode = direction, original_text = text, shift_amount = shift)
    again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")

    







