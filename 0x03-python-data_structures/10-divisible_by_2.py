#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new = []
    isMul = True
    notMul = False
    for item in my_list:
        if item % 2 == 0:
            new.append(isMul)
        else:
            new.append(notMul)
    return new
