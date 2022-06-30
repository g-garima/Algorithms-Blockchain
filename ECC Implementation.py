import hashlib
import random
from math import *

p=11    
a, b = -7, 10
G=(3,4)

def f(x,a,b):
        return x**3+a*x + b

def bits(n):
        while n:
            yield n & 1
            n >>= 1

def modInverse(a, p):
     
    for x in range(1, p):
        if (((a%p) * (x%p)) % p == 1):
            return x
    return -1

def add(P, Q):
    xp, yp = P
    xq, yq = Q

    if (P==(0,0)) and (Q==(0,0)): # check for the zero point 
        return P
    
    elif (xp==-xq) and (yp==-yq):
        return (0,0)

    elif (P==(0,0)) or (Q==(0,0)):
        if(P==(0,0)):
            return Q
        else:
            return P

    elif (P!=Q):
        y1 = (yp - yq) 
        x1 = (xp - xq)

        if (x1<0):
            if(abs(x1)<p):
                x1 = p + x1
            elif(abs(x1)>p):
                x1 = (x1 % p) 

        inv_x1 = modInverse(x1, p) 
        m =(y1* inv_x1) % p
        xr = ((m*m) - xp - xq) % p
        yr = (m * (xp - xr) - yp) % p
        return (xr, yr)

    elif (P==Q):
        return (double(P))

def double(P):
    xp, yp = P
    y1=((3*(xp*xp))+a)
    x1=(2*yp)
    inv_x1 = modInverse(x1, p) 
    m =(y1* inv_x1) % p
    xr = ((m*m) - xp - xp) % p
    yr = (m * (xp - xr) - yp) % p
    return (xr, yr)
       
def double_and_add(n, P):
    result = (0,0)
    addend = P
    for b in bits(n):
        if b:
            result = add(result, addend)
        addend = double(addend)
    return result

print(double_and_add(3,(1,-2)))
print()
print()
str = "DEMOTEXT"
result = hashlib.sha1(str.encode())
z=int(result.hexdigest(),20)
print("The integer message digest of SHA1 : ", z)

k=random.randint(11,999)

priv=random.randint(10,99)
pub=double_and_add(priv,G)
P=double_and_add(k,G)

xp,yp=P
R=xp

inv_k=modInverse(k,p)

S=(inv_k * ( z + priv * R))%p
print("Signature : ",S)

inv_s=(modInverse(S,p))%p
res1=double_and_add(z,G)
res2=double_and_add(R,pub)
p1=double_and_add(inv_s,res1)
p2=double_and_add(inv_s,res2)
checkP=(add(p1,p2))

x_checkp, y_checkp=checkP

if(R==x_checkp):
    print("ECDSA is VERIFIED")

else:
    print("ECDSA not VERIFIED")

print()
print()






