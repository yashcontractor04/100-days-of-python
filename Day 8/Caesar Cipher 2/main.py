alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text, shift_amount):
    # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
    #  by the shift amount and print the decrypted text.
    decrypted_text = ""
    for letter in original_text:
        if letter == " ":
            decrypted_text += " "
            continue
        original_position = alphabet.index(letter) - shift_amount
        original_position %= len(alphabet)
        decrypted_text += alphabet[original_position]
    print(f"Here is the decoded result: {decrypted_text}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(input_text, shift_amount, encode_or_decode):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        if letter == " ":
            output_text += " "
            continue
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount=shift)
caesar(input_text=text, shift_amount=shift, encode_or_decode=direction)


