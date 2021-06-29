import time
from Crypto.Util.number import *
flag = [REDACTED]
p = getPrime(1024)
q = getPrime(1024)
e = 2**16+1
n=p*q
ciphertext=[]
for ch in flag:
    ciphertext.append((ord(ch)**e)%n)
print(n)
print(e)
print(ciphertext)
