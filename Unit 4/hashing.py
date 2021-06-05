import pickle
import hashlib

# If credentials file exists open it, otherwise create it.
try:
    open("./Unit 4/credentials.pkd", "xb")
    print("Credentials created")
except:
    print("Credentials loaded")

with open("./Unit 4/credentials.pkd", "rb") as cred_file:
    # if credential file contains a dictionary, load it, otherwise create one
    try:
        creds = pickle.load(cred_file)
    except:
        creds = {}

# get and convert values
username = input("Username: ")
password = input("Password: ")
hashed_pass = hashlib.md5(password.encode('utf-8')).hexdigest()

# new user, add to credentials
if username not in creds.keys():
    creds[username] = hashed_pass
    print("Credentials added")
    with open("./Unit 4/credentials.pkd", "wb") as cred_file:
        pickle.dump(creds,cred_file)
# return users check if passwords match
else:
    if creds[username] == hashed_pass:
        print("Welcome")
    else:
        print("Wrong username or password")
