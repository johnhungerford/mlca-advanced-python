from typing import List, Any

from utilities.test_runner import TestRunner


def two_sum(nums: List[int], target: int) -> (int, int):
    """
    Find two elements in a list of integers (nums) that add up to given target integer (target).
    Assume that there will only be one pair of integers that adds up to the target. Return the
    indices of the two elements in any order.
    """
    return None, None


class Runner(TestRunner):
    def run_function(self, test_case: dict):
        nums = test_case['nums']
        target = test_case['target']
        return two_sum(nums, target)

    def compare_result(self, actual, expected) -> bool:
        return set(actual) == set(expected)


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

if __name__ == '__main__':
    test_runner = Runner(test_cases)
    test_runner.run_tests()
