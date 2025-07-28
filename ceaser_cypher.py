# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 13:38:40 2025

@author: ahmed amr ahmed khalil
"""
###ceaser_cypher
#lower case upper case  symbols numbers
import string

def ceaser_cypher(message,shift):
    ascii = string.ascii_lowercase + string.ascii_uppercase
    ascii = ascii + string.punctuation+ string.digits
    result2 = ""
    for char in message:
        index = 0
        while(char != ascii[index]):#instead of this you could have used the index() function directly
            index += 1
        if(char.islower()):
            char = ascii[(index+shift)%26]
        elif(char.isupper()):
            char = ascii[((index - 26 + shift) % 26) + 26]
        elif(char.isdigit()):
            char = ascii[(index- 84 +shift)%10 +84]
        else:
            char = ascii[(index- 52 +shift)%32 + 52]
        result2 += char
    return result2

IsFinished = 1
print("Welcome to Ceaser Cypher!")
while(IsFinished != 0):
    mode = int(input("do you want to encode(1) or decode(2): "))
    message = input("please enter the message: ")
    shift = int(input("please enter the shift number: "))
    if(mode == 1):
        Encoded_result=ceaser_cypher(message,shift)
        print(f"the encoded message is: {Encoded_result}")
    elif(mode == 2):
        Decoded_result=ceaser_cypher(message,-1*shift)
        print("the decoded message is: ",Decoded_result)
    else:
        mode = int(input("invalid input please try again: "))
    IsFinished = int(input(("If you wish to continue press 1 else press 0: ")))




























