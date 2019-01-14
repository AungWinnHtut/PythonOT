#!/usr/bin/python3
# Min number finding

min_no = 9999999
i = 0
while i >= 0:
    i = int(input('Please Enter an Int: '))
    if i < min_no:
        min_no = i
    print(min_no)


