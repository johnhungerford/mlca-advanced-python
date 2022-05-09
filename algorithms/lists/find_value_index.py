from typing import List

from utilities.test_runner import TstRunner


# Copy this function
def find_value_index(nums: List[int], target: int) -> int:
    """This function searches a *sorted* list of numbers (ascending order) for a
       target value. If it finds the value it returns its index. If it does not
       find the value, it returns the index where that value would be if it were in the list"""
    pass

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
    {
<<<<<<< HEAD
        'nums': list(range(0,1000000000)),
        'target': 100000001,
        'expected': 100000001,
    }
=======
        'nums': list(range(0, 10000000)),
        'target': 9999998,
        'expected': 9999998,
        'timeout': 1,
    },
>>>>>>> main
]

test_find_value_index = TstRunner(test_cases=test_cases,
                                  arg_extractor=lambda case: [case['nums'], case['target']])
