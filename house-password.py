#!/usr/bin/env python
# encoding: utf-8
"""
house-password.py

Created by Peter Evans on 2014-02-14.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

def checkio(data):
    upper = 0
    lower = 0
    num = 0
    if len(data) > 9:
        for i in data:
            if i.isdigit():
                num+=1
            elif i.islower():
                lower+=1
            elif i.isupper():
                upper+=1
        if (num > 0) and (lower > 0) and (upper > 0):
            return True
        else:
            return False
    else:
        return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

