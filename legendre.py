#!/usr/bin/python3.6
from math import sqrt, ceil
import sys

a = int(sys.argv[1])
p = int(sys.argv[2])
factors = []


def is_prime(n): # aks primality test
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def all_prime(x):
    for i in x:
        if not is_prime(i):
            return False
    return True

def is_square(n):
    if n < 0:
        return False
    return sqrt(n).is_integer()

def fermat_factor(n):
    if is_prime(n):
        return [n]
    if n % 2 == 0:
        factors.append(2)
        factors.append(n//2)
        return [2, n//2]
    a = ceil(sqrt(n))
    b2 = a**2 - n
    while not is_square(b2):
        a += 1
        b2 = a**2 - n
    p = int( a - sqrt(b2) )
    q = int( a + sqrt(b2) )
    factors.append(p)
    factors.append(q)
    return [p, q]

def legendre(a,p):
    assert(p % 2 != 0 and is_prime(p) and a % p != 0)
    print("(", a, "/", p, ")")
    if a == -1:
        return int((-1)**((p-1)/2))
    elif a == 2:
        return int((-1)**((p**2 - 1)/8))
    elif is_square(a):
        return 1
    elif a % p < a:
        return legendre(a % p, p)
    elif a < 0:
        return legendre(-1, p) * legendre(abs(a), p)
    elif not is_prime(a):
        b, c = fermat_factor(a)
        return legendre(b, p) * legendre(c, p)
    if a % 4 == 3 and p % 4 == 3:
        return -legendre(p, a)
    else:
        return legendre(p, a)

print(str(legendre(a,p)))
