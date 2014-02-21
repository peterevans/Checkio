#!/usr/bin/env python
# encoding: utf-8

def checkio(array):
    if len(array) == 0:
        return 0
    else:
        last = array[len(array)-1]
        evens = array[::2]
        total = 0
        for i in evens:
            total = total + i
        return total * last


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "Empty"