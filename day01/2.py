#!/usr/bin/env python3

## Adevent of code -- day 01/P02 ----------- By Abdellah Lafia
##___________________________________________________________

with open('input2.txt', 'r') as f:
    s = [int(x) for x in f.readlines()]
print(len([x for x in range(3,len(s)) if sum(s[x-2:x+1]) > sum(s[x-3:x])]))

