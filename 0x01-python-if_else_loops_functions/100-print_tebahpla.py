#!/usr/bin/python3
i = 0
for j in range(ord('z'), ord('a') - 1, -1):
    if j % 2 == 0:
        i = 0
    else:
        i = 32
    print("{}".format(chr(j - i)), end="")
