def checkPassword(text):
  result = ""
  for i in range(len(text)):
    char = ord(text[i])
    result += chr(char^(i+13))
  return result == "kbnwjvvuqIu+*|Dssrf]"

userInput = input("Oh, you want to enter the kitchen? I need a warrant.\n")

if (checkPassword(userInput)):
  print("Fine, come in.")
else:
  print("That's not right!")
