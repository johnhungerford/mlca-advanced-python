from typing import List, Any, Optional

from utilities.test_runner import TestRunner


def validate_brackets(expression: str) -> bool:
    """
    Given a string containing, among other characters, '[', ']', '{', '}', '(',
    and ')', return true if the brackets/parentheses are used in a valid manner.

    Requirements for valid bracketing:
    1. No closing bracket (']', '}', or ')') can precede an opening bracket ('[', '{', or '(')
    2. Every opening bracket must be followed by a closing bracket at some point
    3. No closed bracket pair can enclose an unclosed bracket pair (e.g. '[{}]' is valid, but '[{]}'
       is not valid.
    """
    pass


class Runner(TestRunner):
    def run_function(self, test_case: dict):
        expression = test_case['expression']
        return validate_brackets(expression)

test_cases = [
    {
        'expression': "{  }hello[---](world)",
        'expected': True,
    },
    {
        'expression': "abc{[(hello)]}def",
        'expected': True,
    },
    {
        'expression': "{]",
        'expected': False,
    },
    {
        'expression': "{}]",
        'expected': False,
    },
    {
        'expression': "[(i + 2) * 3 for i in range(0, 500)]",
        'expected': True,
    },
    {
        'expression': "[(i + 2) * 3 for i in range(0, 500})]",
        'expected': False,
    },
]

if __name__ == '__main__':
    test_runner = Runner(test_cases)
    test_runner.run_tests()
