"""

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
    Q   Q The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

"""
Logic: 
Assuming difference between consecutive numbers in the arranged array is 1 and not haphazard, then
1. sort the array
2. find the minimum integer in the array,
3. traverse through the array from that integer by a step of 1
4. if result exists in array, move on to the next integer,
    if not then display that integer


"""


def find_missing_integer(array):
    array.sort()
    for i in range(min(array), max(array)+1, 1):
        if i == max(array):
            """ cases: if max(array) = 0, if max(array) = -ve or if max(array) = +ve"""
            if i <= 0:
                return 1
            else:
                i += 1
                return i
        elif i in array or i <= 0:
            continue
        else:
            return i


user_input = [3, 4, -1, 1, 4, 1, -10]

print(find_missing_integer(user_input))
