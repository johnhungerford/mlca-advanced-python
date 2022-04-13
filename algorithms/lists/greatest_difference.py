from typing import List

from utilities.test_runner import TestRunner


def greatest_difference(nums: List[int]) -> (int, int):
    """Find the two indices that have the greatest difference between them. If there are multiple
       pairs with the greatest difference, return the *lowest two*. Return the indices as a tuple
       in ascending order (e.g., (3, 5), not (5, 3))"""
    pass


test_cases = [
    {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'expected': (0, 8),
    },
    {
        'nums': [9, 8, 7, 6, 5, 4, 3, 2, 1],
        'expected': (0, 8),
    },
    {
        'nums': [600, 325, -259, 23, 5389, 253],
        'expected': (2, 4),
    },

]


class Runner(TestRunner):
    def run_function(self, test_case: dict):
        nums = test_case['nums']
        return greatest_difference(nums)


if __name__ == '__main__':
    test_runner = Runner(test_cases)
    test_runner.run_tests()
