def swap(string, i1, i2):
    if (i2 == len(string)):
        return string[i1]
    return (string[i2] + string[i1])

def checkFlag(flag):
    result = ""
    for i in range(len(flag)):
        result += flag[(i-5)%len(flag)]

    result2 = ""
    for i in range(0,len(result),2):
        result2+=swap(result,i,i+1)

    result3 = ""
    for char in result2:
        result3 += chr(ord(char)-10)

    return result3 == "'Z&d\sWbq]fid_iekWkhUi)XjiU"



userInput = input("What is the truly best dinosaur? ")

if (checkFlag(userInput)):
    print("You got it right! Congrats, and hope you had a great stay at Jurassic Park.")
else:
    print("Incorrect. Try again.")


flag = "flag{spinosaurus_b3st_d1n0}"