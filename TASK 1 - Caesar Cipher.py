# TASK 1 - Caesar Cipher

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(text, shift):
    result = ""

    for letter in text:
        if letter.lower() in alphabet:
            # find where the letter sits in the alphabet (a=0, b=1, ...)
            position = alphabet.index(letter.lower())

            # move it forward by the shift, and wrap around after z
            new_position = (position + shift) % 26
            new_letter = alphabet[new_position]

            # keep capital letters capital
            if letter.isupper():
                new_letter = new_letter.upper()

            result = result + new_letter
        else:
            # spaces, numbers, punctuation stay the same
            result = result + letter

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# ---- main program ----
text = input("Enter your text: ")
shift = int(input("Enter shift number: "))
choice = input("Type 'e' to encrypt or 'd' to decrypt: ")

if choice == "e":
    print("Result:", encrypt(text, shift))
elif choice == "d":
    print("Result:", decrypt(text, shift))
else:
    print("Please type e or d")