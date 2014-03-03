#!/usr/bin/env python
# encoding: utf-8

def checkio(text):
    total = 0
    lower = text.lower()
    most = lower[0]
    for i in lower:
        if i.isalpha():
            if lower.count(i) > total:
                most = i
                total = lower.count(i)
            elif lower.count(i) == total:
                if i < most:
                    most = i
                    total = lower.count(i)
    return most
        
    #replace this for solution
    return 'a'

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
