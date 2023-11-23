#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)

    if num == 1:
        print(f"0 arguments.")
    elif num == 2:
        print(f"{num - 1} argument:")
        print(f"{num - 1}: {sys.argv[num - 1]}")
    else:
        mess = "arguments:"
        print(f"{num - 1} {mess}")
        for i, ele in enumerate(sys.argv):
            if i != 0:
                print(f"{i}: {ele}")
