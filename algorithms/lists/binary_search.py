import sys
import time
from typing import List

from utilities.test_runner import TestRunner


def find_target_index(nums: List[int], target: int) -> int:
    """This function searches a *sorted* list of numbers (ascending order) for a
       target value. If it finds the value it returns its index. If it does not
       find the value, it returns the index where that value would be if it were in the list"""
    pass


class Runner(TestRunner):
    def run_function(self, test_case: dict):
        nums = test_case['nums']
        target = test_case['target']
        find_target_index(nums, target)


test_cases = [
    {
        'nums': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'target': 6,
        'expected': 6,
    },
    {
        'nums': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'target': 11,
        'expected': 11,
    },
    {
        'nums': [2, 4, 6, 8, 10, 12, 14],
        'target': 11,
        'expected': 5,
    },
]


if __name__ == '__main__':
    test_runner = Runner(test_cases)
    test_runner.run_tests()
