#!/usr/bin/env python3

## Adevent of code -- day 03/P01 ----------- By Abdellah Lafia
##_____________________________________________________________

with open("input.txt", "r") as f:
    s = f.readlines()
o, z = 0, 0
g, e = [], []

for i in range(len(s[0])-1):    
    for j in s:
        if int(j[i]) == 1:
            o += 1 
        else:
            z += 1
        
    if z>o:
        g.append('0')
        e.append('1')
    else:
        g.append('1')
        e.append('0')
    o,z = 0,0

g = int(''.join(g),2)
e = int(''.join(e),2)
print(g*e)


