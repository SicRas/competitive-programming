# Akash Kandpal
# My Domain => http://harrypotter.tech/
from fractions import gcd
import math
from itertools import permutations

def readInts():
    return list(map(int, raw_input().strip().split()))
def readInt():
    return int(raw_input())
def readIntsindex0():
    return list(map(lambda x: int(x) - 1, input().split()))
def readStrs():
    return raw_input().split()
def readStr():
    return raw_input()
def numlistTostr(list1):
    return ''.join(list1)
def strlistTostr(list1):
    return ''.join(str(e) for e in list1)
def strTolist(str):
    return str.split()
def strlistTointlist(str):
    return map(int, str)
def slicenum(number,x):
    return int(str(number)[:x])
def precise(num):
    return "{0:.10f}".format(num)
def rsorted(a):
    return sorted(a,reverse=True)
def binar(x):
    return '{0:031b}'.format(x)
def permute(word):
    perms = [''.join(p) for p in permutations(word)]
    # print perms
    return set(perms)

arr = []
for __ in range(readInt()):
    stri = readStr()
    a = []
    for i in stri:
        if(ord(i)>96):
            a +=chr(27-(ord(i)-96)+96)
        else:
            # print ord(i)
            a +=chr(27-(ord(i)-64)+64)
    # print a
    print(strlistTostr(a))

'''
5
aaaaaa
axycd
dasafdssfsa
abcdefghijklmnopqrstuvwxyz
ABCas
'''
