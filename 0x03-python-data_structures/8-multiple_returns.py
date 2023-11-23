#!/usr/bin/python3
def multiple_returns(sentence):
    lenn = len(sentence)
    if sentence == "":
        ch = None
    else:
        ch = sentence[0]
    return ((lenn, ch))
