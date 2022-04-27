#!/usr/bin/env python3

## Adevent of code -- day 03/P02 ----------- By Abdellah Lafia
##_____________________________________________________________

#with open('input.txt', 'r') as f:
#    s = [ x.strip() for x in f.readlines()]

s =[ '00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

def molc(): # Most or least common
    o, z = 0, 0 
    mc, lc = [], [] 
      
    for i in range(len(s[0])):
        for j in s:
            if int(j[i]) == 1:
                o += 1
            else:
                z += 1
        
        mc.append('1') if o>=z else mc.append('0')
        lc.append('1') if o<=z else lc.append('0')
        o,z = 0, 0
    return mc,lc 
#________________________^______PART 1_________^__________________________#

def filter_(array1, array2, p=0):
    if p == len(array2) or len(array1) == 1:
        return array1[0]
    new_array = []
 
    for i in array1:
        #check if there is a matching common
        if len(array2) == 2:

        if i[p] == array2[p]:
            new_array.append(i)
    p += 1
    return filter_(new_array, array2, p)

def lsr(): #Life Support Rating
    mc, lc = molc()
    
    o2 = filter_(s,mc)
    co2 = filter_(s,lc)
    
    print(int(''.join(o2),2)*int(''.join(co2),2))
lsr()
#this is an incomplete solution, will continue tomorrow
