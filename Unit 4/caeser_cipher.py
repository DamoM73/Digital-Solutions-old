# get inputs
message = input("Enter message: ")
key = int(input("Enter key: "))

# create variables
alphabet = "abcdefghijklmnopqrstuvwxyz "
encrypt = ""
decrypt = ""

# encrypting
for letter in message:
    pos = alphabet.find(letter)
    newpos = (pos + key) % 27
    encrypt += alphabet[newpos]

print(encrypt)

# decrypting
for letter in encrypt:
    pos = alphabet.find(letter)
    newpos = (pos - key) % 27
    decrypt += alphabet[newpos]

print(decrypt)