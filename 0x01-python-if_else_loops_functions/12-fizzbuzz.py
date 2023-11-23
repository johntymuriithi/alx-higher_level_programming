#!/usr/bin/python3
f = "Fizz"
b = "Buzz"
a = "FizzBuzz"


def fizzbuzz():
    for num in range(1, 101):
        if num == 100:
            print(f"{b} ", end="")
        elif num % 3 == 0 and num % 5 == 0:
            print(f"{a} ", end="")
        elif num % 3 == 0:
            print(f"{f} ", end="")
        elif num % 5 == 0:
            print(f"{b} ", end="")
        else:
            print(f"{num} ", end="")
