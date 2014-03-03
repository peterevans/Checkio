#!/usr/bin/env python
# encoding: utf-8

def checkio(number):
    binary = str(bin(number))
    return binary.count(str(1))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9