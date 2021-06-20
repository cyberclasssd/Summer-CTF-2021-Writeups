p = 83625243486278694472415908934747878517015029114727455464007997523526728908861
q = 72586358108422808800129663277207723787974454196650071835769584762231832455893 #these will not be used.
e = 3
c = 199928678441516785442874823915652326973813168371198052837348340429140512331159192676977946213961036591363169714191827729475745587917927733953125

def find_invpow(x,n):    
    high = 1
    while high ** n < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

m = find_invpow(c, e) #find the cube root of c to find m

m = hex(m)[2:] #decimal -> hex
m = bytes.fromhex(m) #hex -> ascii
print(m.decode()) #print the flag
