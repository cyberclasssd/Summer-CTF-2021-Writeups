import base64
def revFlag(flag):
    result = ""
    for char in flag:
        result += chr(ord(char) + 13)
    flag = base64.b64decode(result.encode('ascii')).decode('ascii')
    print(flag)

revFlag("M`k[M&g(@;HaW]AYLJA#@KM[W7A^K%$(K&ElLK5YL%9lM69,")

