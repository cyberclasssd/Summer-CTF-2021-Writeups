def swap(string, i1, i2):
    if (i2 == len(string)):
        return string[i1]
    return (string[i2] + string[i1])
def revFlag(flag):
    result = ""
    for char in flag:
        result += chr(ord(char)+10)

    result2 = ""
    for i in range(0,len(result),2):
        result2+=swap(result,i,i+1)

    result3 = ""
    for i in range(len(result2)):
        result3 += result2[(i+5)%len(result2)]

    print(result3)

revFlag("'Z&d\sWbq]fid_iekWkhUi)XjiU")