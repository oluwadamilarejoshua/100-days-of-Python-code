
from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(dir = direction, txt = text, sft = shift):
    my_alph = alphabet * 2
    text_to_return = ""
    position = 0
    new_position = 0
    if dir == "decode":
        sft *= -1
        new_position += 26
    for letter in txt:
        position += alphabet.index(letter)
        new_position += sft
        text_to_return += my_alph[new_position]

    print(f"The {dir}d text is {text_to_return}")


ceasar(dir = direction, sft = shift, txt = text)