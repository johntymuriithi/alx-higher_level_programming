#!/usr/bin/python3
num = 0
output = ""
while num < 100:
    if num <= 9:
        output += "0{}, ".format(num)
    elif num == 99:
        output += "{}".format(num)
    else:
        output += "{}, ".format(num)
    num += 1
print(output)
