"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all

the numbers in the original array except the one at i. For example, if our input was [1, 2, 3, 4, 5], the expected

output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""
from Problem2_functions import product


example_input = [10, 12, 32, 24, 15]

if 0 in example_input:
    output = [0] * len(example_input)
    print(f'Your array has a \'zero\' in it and therefore the product is :{output} ')
else:
    print(product(example_input))

example_input.remove(example_input[0])
print(example_input)
