from typing import List, Tuple

from utilities.tests_runner import TestRunner


# Copy this function
def greatest_difference(nums: List[int]) -> Tuple[int, int]:
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

test_greatest_difference = TestRunner(test_cases=test_cases,
                                      arg_extractor=lambda case: [case['nums']])
