"""
How to structure a test:
1. WHat do you want to test?
2. Are you writing a unit test oor an integration test
Decide above then:
1. Create your inputs
2. Execute the code being tested, capturing the output
3. Compare the output with the expected result

For <summer> testcases:
1. CAn it sum up a list of integers?
2. Float?
3. Can it sum tuples or sets
4. Can it sum negative values
5. What happens when you provide a bad value like a single integer or a str
6. What if you give a generator object as argument
"""

import unittest

from Testing_and_test_cases.my_sum.summer import sum_func


class TestSummer(unittest.TestCase):

    def test_list_int(self):
        """
        Test if Summer can sum integers
        """
        data = [1, 2, 3]
        result = sum_func(data)
        self.assertEqual(result, 6, "Cannot sum over integers")


if __name__ == '__main__':
    unittest.main()
