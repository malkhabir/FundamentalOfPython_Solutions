"""
This script does a quick decrypt encrypt using the ord() and chr().
This was done with no explicit declaration of a list data type.
"""

import os

distance = int(input("Enter the distance value: "))
code = ""
plainTexte = ""
cipherValue = 0
cipherValuee = 0
ordValue = 0
ordValuee = 0


# Opening the correct file in the directory
myDirectory = os.getcwd()
filenames = os.listdir(myDirectory)
entered = input("Enter your file name: ")

for files in filenames:
    if entered == files:
        f = open(entered, "r", newline='\n')

        # Encryption
        print("######################### Encryption #########################")
        readFile = f.readlines()

        for sentences in readFile:
            # Encryption
            for ch in sentences:
                ordValue = ord(ch)
                cipherValue = ordValue + distance
                code = code + chr(cipherValue)
        print(code)

    elif entered != files:
        continue

# Decryption
wrongNumber = int(input("Enter your distance key: "))
print("######################### Decryption ###########################")
for i in code:
    ordValuee = ord(i)
    cipherValuee = ordValuee - wrongNumber
    plainTexte += chr(cipherValuee)
print(plainTexte)
