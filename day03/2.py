#!/usr/bin/env python3

## Adevent of code -- day 03/P02 ----------- By Abdellah Lafia
##_____________________________________________________________

with open('input.txt', 'r') as f:
    s = [ x.strip() for x in f.readlines()]

def molc(a,t,p): # Most or least common (array, type, position)
    o, z = 0, 0 # counters 
     
    if len(a) == 2:
        return t 
    for i in a:
        if int(i[p]) == 1:
            o += 1
        else:
            z += 1
    if t == 1:
        return 1 if o>=z else 0
    if t == 0:
        return 0 if o>=z else 1
           
def filter_(a, t, p=0):
    # loop over cols of a 2d array and cmp each element with most or least common    
    if p == len(a[0]) or len(a) == 1: # exit recursion
        return a[0]

    new_a = []
    c = molc(a,t,p) # most or least common bit
    for i in a: 
        if int(i[p]) == c:
            new_a.append(i)
    p += 1
    return filter_(new_a,t, p)

def lsr():              #Life Support Rating
    o2 = filter_(s,1)   # 1 for O2, 0 for CO2
    co2 = filter_(s,0)
    print(int(''.join(o2),2)*int(''.join(co2),2))
lsr()
