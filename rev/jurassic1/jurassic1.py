def checkFlag(password):
  print(password[::-1])
  return password[::-1] == "}cons_onid_cissaruj{galf"

userInput = input("Please enter the correct flag: ")

if (checkFlag(userInput)):
  print("YEs")
else:
  print("nno")
