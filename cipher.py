alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("W3LC0M3 A6ENT5, T0 TH3 C1PH3R, Y0U'R3 M1$$10N 15 T0 N0T G3T C@U6HT...\n\n")


def codex(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Encrypted message: {end_text}\n\n")

game_over = False
while not game_over:

    direction = input("Type 'encode' or 'decode':\n")
    text = input("What is your message?:\n").lower()
    shift = int(input("Enter the shift number:\n"))

    shift = shift % 26

    codex(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'y' to cipher again. To end type 'n'.\n")
    if restart == "n":
        game_over = True
        print("Program will self destruct in five seconds.")
