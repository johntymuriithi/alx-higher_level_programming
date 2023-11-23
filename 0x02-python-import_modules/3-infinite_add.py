#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0

    for i, ele in enumerate(sys.argv):
        if i == 0:
            continue
        num = int(ele)
        sum += num

    print(f"{sum}")
