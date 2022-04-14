from typing import List, Any, Optional

from utilities.test_runner import TestRunner


def most_common_element(elements: List[Any]) -> List[Any]:
    """
    In a list of values of a given type (any type that can be compared with ==), return
    a list of the most common element values. For instance, in the list [0, 1, 0, 2, 0, 3, 3, 3, 4, 2]
    there are three 0s, three 3s, two 2s, one 1 and one 4, so the correct solution is [0, 3]
    or [3, 0].
    """
    return [None]


class Runner(TestRunner):
    def run_function(self, test_case: dict):
        elements = test_case['elements']
        return most_common_element(elements)

    def compare_result(self, actual, expected) -> bool:
        return set(actual) == set(expected)


test_cases = [
    {
        'elements': [0, 1, 2, 3, 1],
        'expected': [1],
    },
    {
        'elements': [0, 0, 1, 1, 2, 2, 3],
        'expected': [0, 1, 2],
    },
    {
        'elements': [0, 1, 1, 2, 1, 2, 1, 3, 1],
        'expected': [1],
    },
    {
        'elements': [5 if i % 100 == 0 else i for i in range(0, 1000)],
        'expected': [5],
    },
]

if __name__ == '__main__':
    test_runner = Runner(test_cases)
    test_runner.run_tests()