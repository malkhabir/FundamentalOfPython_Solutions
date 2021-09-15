plainText = input("Please enter the text to encrypt: ")
distance = int(input("Enter the distance value: "))
code = ""
plainTexte = ""

# Encryption
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code += chr(cipherValue)
print(code)

# Decryption
for i in code:
    ordValuee = ord(i)
    cipherValuee = ordValuee - distance
    if cipherValuee < ord('a'):
        cipherValuee = ord('z') + distance - (ord('a') - ordValuee - 1)
    plainTexte += chr(cipherValuee)
print(plainTexte)
