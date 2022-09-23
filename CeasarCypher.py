
from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(txt = text, sft = shift):
    my_alphab = alphabet * 2
    coded_message = ""
    for i in txt:
        position = alphabet.index(i)
        coded_message += my_alphab[position + sft]
    print(f"The encoded text is {coded_message}")
   
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(txt = text, sft = shift):
    my_alphab = alphabet * 2
    extra = 26
    decoded_message = ""
    for i in txt:
        position = alphabet.index(i)
        to_use = position + extra
        decoded_message += my_alphab[to_use - sft]
    print(f"The decoded text is {decoded_message}")

 #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(txt = text, sft = shift)
elif direction == "decode":
    decrypt(txt = text, sft = shift)
else:
    print("Selection not valid")

