from typing import List, Tuple

from utilities.test_runner import TstRunner

# Copy this function
def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Find two elements in a list of integers (nums) that add up to given target integer (target).
    Assume that there will only be one pair of integers that adds up to the target. Return the
    indices of the two elements in any order.
    """
    return None, None


test_cases = [
    {
        'nums': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'target': 2,
        'expected': (0, 2),
    },
    {
        'nums': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'target': 18,
        'expected': (8, 10),
    },
    {
        'nums': [2, 4, 6, 7, 10, 12, 14],
        'target': 19,
        'expected': (3, 5),
    },
    {
        'nums': [i for i in range(0, 10001)],
        'target': 1,
        'expected': (0, 1),
    },
    {
        'nums': [i for i in range(0, 10001)],
        'target': 19999,
        'expected': (9999, 10000),
    },
    {
        'nums': [i for i in range(0, 20001)],
        'target': 39999,
        'expected': (19999, 20000),
    },
    {
        'nums': [i for i in range(0, 1000001)],
        'target': 1999999,
        'expected': (999999, 1000000),
    },
]

test_two_sum = TstRunner(test_cases=test_cases,
                         evaluator=lambda a, e: set(a) == set(e),
                         arg_extractor=lambda dict: [dict['nums'], dict['target']])
