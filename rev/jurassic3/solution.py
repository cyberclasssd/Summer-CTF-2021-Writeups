def revFlag(flag):
  result=""
  for char in flag:
    result += chr(ord(char) + 10)
  print(result)

  flag = bytes.fromhex(result).decode()

  print(flag)

revFlag(",,,Y,',--X-*(Z-(,+-.+\,.,'-)+\,+-),),'-&,+,*-Z")
