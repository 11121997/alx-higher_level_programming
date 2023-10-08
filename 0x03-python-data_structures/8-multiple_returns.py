#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
    a1 = len(sentence)
    a2 = sentence[0]
    return a1, a2
