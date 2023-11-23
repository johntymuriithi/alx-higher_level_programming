#!/usr/bin/python3
for charr in range(ord('a'), ord('z') + 1):
    if chr(charr) == 'q' or chr(charr) == 'e':
        continue
    print("{}".format(chr(charr)), end='')
