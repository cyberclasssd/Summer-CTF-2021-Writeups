import binascii

def checkFlag(flag):
  flag = binascii.hexlify(flag.encode()).decode()
  result=""
  for char in flag:
    result += chr(ord(char) - 10)
  
  return result == ",,,Y,',--X-*(Z-(,+-.+\,.,'-)+\,+-),),'-&,+,*-Z"

userInput = input("Please enter the correct password: ")

if (checkFlag(userInput)):
  print("Congrats! You just let the t-rex out!")
else:
  print("What are you doing? Stop it!")
