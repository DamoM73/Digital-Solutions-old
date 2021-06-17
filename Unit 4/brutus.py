# this program accept a cypher and then brut forces through possible decryption

print("Welcome to Brutus, the Caesar destroyer")

no_space = "abcdefghijklmnopqrstuvwxyz"
with_space = "abcdefghijklmnopqrstuvwxyz "

while True:
    spaces = ""
    while spaces not in ["yes","no"]:
        spaces = input("Does the cipher contain spaces? ").lower()
    
    if spaces == "yes":
        alpha = with_space  
    else:
        alpha = no_space

    cipher = input("Enter cipher: ").lower()

    for index in range(len(alpha)):
        decrypt = ""
        for letter in cipher:
            pos = alpha.find(letter)
            newpos = (pos + index) % len(alpha)
            decrypt += alpha[newpos]
        print(decrypt)

    print("\n")