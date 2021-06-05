from cryptography.fernet import Fernet

# if key exists load, otherwise create a key
try:
    with open('./Unit 4/mykey.key', 'rb') as mykey:
        key = mykey.read()
except:
    key = Fernet.generate_key()
    with open('./Unit 4/mykey.key', 'wb') as mykey:
        mykey.write(key)

# create the fernet objext
f = Fernet(key)

# encrypting original file
with open('./Unit 4/grades.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open("./Unit 4/enc_grades.csv","wb") as encrypted_file:
    encrypted_file.write(encrypted)

# decrypting encrypted file
with open("./Unit 4/enc_grades.csv", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open("./Unit 4/dec_grades.csv","wb") as decrypted_file:
    decrypted_file.write(decrypted)