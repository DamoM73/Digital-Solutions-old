import pickle
import hashlib

try:
    open("./Unit 4/creds.pkd", "xb")
    print("Credentials file created")
except:
    print("Credentials file loaded")

with open("./Unit 4/creds.pkd","rb") as cred_file:
    try:
        creds = pickle.load(cred_file)
    except:
        creds = {}

username = input("Username: ")
password = input("Password: ")
hash_pass = hashlib.md5(password.encode("utf-8")).hexdigest()

if username not in creds.keys():
    creds[username] = hash_pass
    print("Credentials added")
    with open("./Unit 4/creds.pkd","wb") as cred_file:
        pickle.dump(creds,cred_file)
else:
    if creds[username] == hash_pass:
        print("Welcome")
    else:
        print("Wrong username or password")