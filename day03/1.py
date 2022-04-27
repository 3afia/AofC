#!/usr/bin/env python3

## Adevent of code -- day 03/P01 ----------- By Abdellah Lafia
##_____________________________________________________________

with open('input.txt', 'r') as f:
    s = [ x.strip() for x in f.readlines()]

def molc(): # Most or least common
    o, z = 0, 0
    mc, lc = [], []

    for i in range(len(s[0])):
        for j in s:
            if int(j[i]) == 1:
                o += 1
            else:
                z += 1
        mc.append('0') if z>o else mc.append('1')
        lc.append('1') if z>o else lc.append('0')
        o,z = 0, 0

    print(int(''.join(mc),2)*int(''.join(lc),2))
molc()
