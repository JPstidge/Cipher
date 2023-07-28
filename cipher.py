import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def countdown():
    count = 3
    print("Program will self destruct in three seconds.")
    while count > 0:
        print(count)
        time.sleep(1)
        count -= 1

    print("BOOM!")



print("W3LC0M3 A6ENT5, T0 TH3 C1PH3R, Y0UR M1$$10N 15 T0 N0T G3T C@U6HT...\n\n")

game_over = False
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



while not game_over:

    correct_entry = False

    while not correct_entry:

        direction = input("Type 'encode' or 'decode':\n")
        if direction != "encode" and direction != "decode":
            print("Reenter your encryption and pay attention this time.")
        elif direction == "encode" or direction == "decode":
            correct_entry = True
    text = input("What is your message?:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    shift = shift % 26




    codex(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'y' to cipher again. To end type 'n'.\n")
    if restart == "n":
        countdown()
        game_over = True


