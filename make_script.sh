#!/bin/bash

# check if params were  entered correctly
[ $# -lt 1 ] &&  printf "[!] \tUsage: $0 number of day,\n\t [EXAMPLE]: $0 1\n\n" && exit 1


DIR=day0$1
# check if the codes directory exist, if not create one.
[ -d $DIR ] && printf "$DIR exist\n" && exit 1 || mkdir $DIR 

for i in {1..2}; do
cat << EOF > $DIR/$i.py
#!/usr/bin/env python3

## Adevent of code -- day 0$1/P0$i ----------- By Abdellah Lafia
##_____________________________________________________________

EOF
done

