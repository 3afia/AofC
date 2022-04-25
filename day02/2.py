#!/usr/bin/env python3

## Adevent of code -- day 02/P02 ----------- By Abdellah Lafia
##_____________________________________________________________

with open("input.txt", "r") as f:
    s = f.readlines()
x, y, aim = 0, 0, 0

for i in s:
    m,n = i.split(" ")[0], int(i.split(" ")[1])
    if m == "forward":
        y += aim * n
        x += n
    elif m == "up":
        aim -= n
    else:
        aim += n
print(x * y)


