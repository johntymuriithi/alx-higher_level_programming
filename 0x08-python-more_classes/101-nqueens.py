#!/usr/bin/python3
import sys, random

if len(sys.argv) == 1:
    exit(1)
args = sys.argv[1:]

if (len(args) > 1):
    print("Usage: nqueens N")
    exit(1)
num = args[0]

try:
    num = int(num)
except ValueError:
    print("N must be a number")
    exit(1)

if num < 4:
    print("N must be at least 4")
    exit(1)
back = []
for _ in range(0, num):
    back = []
    for a in range(0, num):
        x = random.randrange(0, num)
        b = [a, x]
        back.append(b)
    print(back)
    print()
