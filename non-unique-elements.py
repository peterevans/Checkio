#! /usr/bin/env python

"""
Given a list of integers. You should return a list consisting only of
non-unique elements. So you need to remove all unique elements (contains
in given list only once). Don't change order in a list.
Example: [1, 2, 3, 1, 3]. 1 and 3 non-unique elements and result will be
[1, 3, 1, 3].

Input: A list of integers.

Output: A list of integers.
"""

def checkio(data):
    newlist = []
    for i in data:
        if data.count(i) != 1:
            newlist.append(i)
    return newlist

#These "asserts" using only for self-checking and not necessary for auto-testing
	if __name__ == "__main__":
	    assert isinstance(checkio([1]), list), "The result must be a list"
	    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
	    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
	    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
	    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
