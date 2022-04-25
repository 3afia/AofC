#!/usr/bin/env python3

## Adevent of code -- day 02/P01 ----------- By Abdellah Lafia
##_____________________________________________________________

with open("input.txt", "r") as f:
    s = f.readlines()
x,y = 0,0

for i in s:
    m,n = i.split(" ")[0], int(i.split(" ")[1])
    if m == "forward":
        x+=n
    elif m == "up":
        y-=n 
    else:
        y+=n 
print(x*y)
