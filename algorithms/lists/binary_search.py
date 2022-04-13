import time
from typing import List


def find_target_index(nums: List[int], target: int) -> int:
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
]


def run_test_case(test_case: dict) -> (bool, str):
    """Runs a test case, returning (true, '') if it passes, (false, 'expected [correct value],
       returned [incorrect value]') if it fails, and (false, '[error msg]') if an exception is raised"""

    try:
        nums: List[int] = test_case['nums']
        target: int = test_case['target']
        expected: int = test_case['expected']

        actual = find_target_index(nums, target)

        if actual == expected:
            return True, ''

        return False, f'expected {expected}, returned {actual}'

    except Exception as e:
        return False, f'Raised {type(e).__name__}{str(e)}'


if __name__ == '__main__':
    i = 1
    for case in test_cases:
        start_time = time.time()
        passed, msg = run_test_case(case)
        end_time = time.time()
        time_elapsed_ms = (end_time - start_time) * 1000

        if passed:
            print(f'{i}: \033[1;32m Passed!\033[0m ({time_elapsed_ms} milliseconds)')
        else:
            print(f'{i}: \033[1;31m Failed!\033[0m {msg}')

        i += 1
