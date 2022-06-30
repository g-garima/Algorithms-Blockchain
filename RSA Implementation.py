# RSA IMPLEMENTATION

from operator import mod
import random
from math import *

print()
print()
print()
# Function to find gcd of two numbers
def cal_gcd(m, n):
	
	if n == 0:
		return m
	else:
		r = m % n
		return cal_gcd(n, r)
	
	
# Program to find Multiplicative inverse

def extendedEuclideanAlgorithm(a,b):
    if a == 0:
        return 0, 1
    u, v = extendedEuclideanAlgorithm(b % a, a)
    x = v - (b // a ) * u
    y = u
    return x, y

def cal_mulinv(a, b):
	
	r1 = a
	r2 = b
	s1 = int(1)
	s2 = int(0)
	t1 = int(0)
	t2 = int(1)
	
	while r2 > 0:
		
		q = r1//r2
		r = r1-q * r2
		r1 = r2
		r2 = r
		s = s1-q * s2
		s1 = s2
		s2 = s
		t = t1-q * t2
		t1 = t2
		t2 = t
		
	if t1 < 0:
		t1 = t1 % a
		
	return (r1, t1)

# Enter two large prime numbers p and q
p = 1249
q = 1423
n = p * q

#euler totient()
Pn = (p-1)*(q-1) 

# Generate encryption key in range 1<e<Pn
key = []
for i in range(2, Pn):
	
	gcd = cal_gcd(Pn, i)
	
        #check they are co-prime
	if gcd == 1:
		key.append(i)


# Select an encryption key from the above list
e = int(random.choice(key))

# Obtain inverse of encryption key
r, d = cal_mulinv(Pn, e)

if r == 1:
	d = int(d)
	print("Decryption Key: ", d)
	
else:
	print("Multiplicative inverse for the given encryption key does not exist. Choose a different encryption key")


# Enter the message to be sent
M1 = int(input("Enter the message: "))

# Signature is created by sender
S = (M1**d) % n

# Sender sends M1 and S both to receiver. Receiver generates message M2 using the signature S, sender's public key e and product n.
M2 = (S**e) % n

# If M1 = M2 only then receiver accepts the message from sender.

if M1 == M2:
	print("As M1 = M2, Accept the message from sender.")
else:
	print("As M1 not equal to M2, Do not accept the message sent.")

print()
print()
print()





