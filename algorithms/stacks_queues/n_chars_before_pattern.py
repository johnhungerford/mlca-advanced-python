from queue import Queue
from typing import Any, List

from utilities.test_runner import TestRunner


def n_chars_before_pattern(text: str, pattern: str, n: int) -> str:
    """
    Given a string (text), return the substring of a given length (n) leading up to the first
    occurence of a given pattern (pattern).

    For instance, if text is "the quick brown fox jumps over the lazy dog", the pattern is
    "mps", and the given length is 6, return "fox ju". The first occurence of "mps" is right
    after the size characters 'f', 'o', 'x', ' ', 'j', and 'u'.
    """
    pass


class Runner(TestRunner):
    def run_function(self, test_case: dict):
        text = test_case['text']
        pattern = test_case['pattern']
        n = test_case['n']
        return n_chars_before_pattern(text, pattern, n)

test_cases = [
    {
        'text': 'the quick brown fox jumps over the lazy dog',
        'pattern': 'mps',
        'n': 6,
        'expected': 'fox ju',
    },
    {
        'text': ''.join(['a' for i in range(0, 10000)]) + 'bcdefghij',
        'pattern': 'hij',
        'n': 7,
        'expected': 'abcdefg',
    }
]

if __name__ == '__main__':
    test_runner = Runner(test_cases)
    test_runner.run_tests()
