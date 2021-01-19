"""
Practicing using generators.
Refactor the following code to generate the same prime numbers but by using generators.


"""
import unittest
# for n in range(2,20):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f'{n} equals {x} * {n//x}')
#             break
#         else:
#             print(f'{n} is a prime number')


def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n
# Python also allows us to use the else condition with for loops.
# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
# FOr example::
# for i in range(1, 4):
#     print(i)
# else:  # Executed because no break in 'for'
#     print("No Break")

g = prime_generator(20)
assert next(g) == 2, "first number skipped"
print(type(g))
print(next(g))

