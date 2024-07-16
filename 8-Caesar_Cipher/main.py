# Import logo from local art.py module
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    # Create Interim list to hold ciphered letters
    interim_list = []
    for letter in text:
        # Try/Except block to catch ValueErrors in alphabet (When a user enters a none alphabetic character, it doesn't cipher the character)
        try:
            # Find the index in the alphabet of each letter in the text
            alphabet_index = alphabet.index(letter)
            if direction == 'encode':
                # If encode: Add shift number to index
                new_letter_index = alphabet_index + shift
                if new_letter_index >= 26:
                    # If new index exceeds 26, remove 26 from the index to keep it in range
                    new_letter_index -= 26
            elif direction == 'decode':
                # If decode: Subtract shift number to index
                new_letter_index = alphabet_index - shift
                if new_letter_index <= -1:
                    # If new index is less than 0, add 26 to the index to keep it in range
                    new_letter_index += 26
            # Add the letter at the new index to the list
            interim_list.append(alphabet[new_letter_index])
        except ValueError:
            interim_list.append(letter)
    # Join text        
    end_text = "".join(interim_list)
        
    return f"Here's the {direction}d result: {end_text}" 

# Variable to keep ciphering in play
continue_ciphering = True
print(logo)

while continue_ciphering:
    # Take the user input to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # While the user makes a mistake in the direction, ask for it again
    while direction != 'encode' or 'Decode':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Take the user's text input to be cipehred
    text = input("Type your message:\n").lower()
    # Take the shift amount
    shift = int(input("Type the shift number:\n"))
    # If shift amount exceeds letters in the alphabet, use modulus to reduce shift amount
    if shift > 26:
        shift = shift % 26
        
    # Call and print function to cipher        
    print(caesar(direction, text, shift))
    
    # Check if user want to continue ciphering
    user_continue = input('Do you want to continue ciphering? Type "y" or "n": ')
    # If user enters no, end application
    if user_continue == 'n':
        continue_ciphering = False