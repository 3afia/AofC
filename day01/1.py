#!/usr/bin/env python3

## Adevent of code -- day 01/P01 ----------- By Abdellah Lafia
##___________________________________________________________

with open('input.txt', 'r') as f:
    s = [int(x) for x in f.readlines()]
print(len([x for x in range(1,len(s)) if s[x] > s[x-1]]))
