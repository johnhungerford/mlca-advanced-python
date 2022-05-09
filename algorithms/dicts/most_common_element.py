from typing import List, Any

from utilities.test_runner import TstRunner

# Copy this function definition
def most_common_element(elements: List[Any]) -> List[Any]:
    """
    In a list of values of a given type (any type that can be compared with ==), return
    a list of the most common element values. For instance, in the list [0, 1, 0, 2, 0, 3, 3, 3, 4, 2]
    there are three 0s, three 3s, two 2s, one 1 and one 4, so the correct solution is [0, 3]
    or [3, 0].
    """
    return [None]


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

test_most_common_element = TstRunner(test_cases=test_cases,
                                     arg_extractor=lambda dict: [dict['elements']])
