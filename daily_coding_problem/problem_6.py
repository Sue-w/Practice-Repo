"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""
# assuming it's upto 5 characters
""" 
1. shift one character from string1 and match with string2. 
2. repeat until match is found.
3. if string length reached return false
"""

a = 'abcde'
b = 'abcde'


def shift_a_to_get_b(a,b):
    length_a = len(a)
    length_b = len(b)
    if length_a != length_b:
        return 'False'
    else:
        i = 1
        while i <= length_a:
            x = a[0]
            a = a.replace(a[0], "")
            a += x
            if a == b:
                return 'True'
            elif i == length_a:
                if a != b:
                    return 'False'
            else:
                i += 1
                continue


print(shift_a_to_get_b(a, b))
