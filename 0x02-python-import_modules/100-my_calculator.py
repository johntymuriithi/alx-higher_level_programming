#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) < 3 or len(sys.argv) - 1 == 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if len(sys.argv) - 1 == 0 or len(sys.argv) - 1 == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[3])
    valid = sys.argv[2]
    allow = ['+', '-', '*', '/']
    if valid not in allow:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if valid == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif valid == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif valid == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif valid == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
