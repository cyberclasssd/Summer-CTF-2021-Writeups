p = 292338524084442490086181008854015675609
q = 185247202893447754330736379123444704803
n = p*q
d = 48913511277713132682013283111754848943415678659992063997085103947173699280865

m = pow(c,d,n) #rsa decryption; m = c^d mod n. this returns a decimal number.

m = hex(m)[2:] #decimal -> hex
m = bytes.fromhex(m) #hex -> ascii

print(m.decode()) #print the flag
