import base64

def checkFlag(flag):
    flag = base64.b64encode(flag.encode('ascii')).decode('ascii')
    result = ""
    for char in flag:
        result += chr(ord(char) - 13)

    return result == "M`k[M&g(@;HaW]AYLJA#@KM[W7A^K%$(K&ElLK5YL%9lM69,"

userInput = input("Enter the passphrase to active the trap: ")

if (checkFlag(userInput)):
    print("Congrats! The T-rex fell for your trap!")
else:
    print("That's not right! Hurry up, the T-rex won't wait for you!")