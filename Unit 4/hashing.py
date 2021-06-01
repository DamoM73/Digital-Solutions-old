import pickle
import hashlib

try:
    open("./Unit 4/credentials.pkd", "xb")
    print("Credentials created")
except:
    print("Credentials loaded")

with open("./Unit 4/credentials.pkd", "rb") as cred_file:
    try:
        creds = pickle.load(cred_file)
    except:
        creds = {}

username = input("Username: ")
password = input("Password: ")
hashed_pass = hashlib.md5(password.encode('utf-8')).hexdigest()

if username not in creds.keys():
    creds[username] = hashed_pass
    print("Credentials added")
    with open("./Unit 4/credentials.pkd", "wb") as cred_file:
        pickle.dump(creds,cred_file)
else:
    if creds[username] == hashed_pass:
        print("Welcome")
    else:
        print("Wrong username or password")

#print(creds)