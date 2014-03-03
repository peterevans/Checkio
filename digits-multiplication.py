#!/usr/bin/env python
# encoding: utf-8

def checkio(number):
    string = str(number)
    product = 1
    for i in string:
        if int(i) != 0:
            product = product * int(i)
    return product

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1