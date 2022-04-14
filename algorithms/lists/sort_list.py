from typing import List

from utilities.test_runner import TestRunner


# Copy this function
def sort_list(nums: List[int]) -> List[int]:
    """Return the same list of integers, sorted in ascending order. Identical numbers should be
       grouped together and not deduplicated."""
    pass


test_cases = [
    {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'expected': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    },
    {
        'nums': [9, 8, 7, 6, 5, 4, 3, 2, 1],
        'expected': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    },
    {
        'nums': [2, 3, 9, 1, 5, 4, 7, 6, 8],
        'expected': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    },
    {
        'nums': [2, 3, 9, 2, 5, 5, 1, 5, 4, 2, 7, 6, 1, 8],
        'expected': [1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9],
    },
]

test_sort_list = TestRunner(test_cases=test_cases, arg_extractor=lambda case: [case['nums']])
