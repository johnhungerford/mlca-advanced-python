from queue import Queue
from typing import Any, List

from utilities.test_runner import TstRunner


# Copy this function
def n_chars_before_pattern(text: str, pattern: str, n: int) -> str:
    """
    Given a string (text), return the substring of a given length (n) leading up to the first
    occurence of a given pattern (pattern).

    For instance, if text is "the quick brown fox jumps over the lazy dog", the pattern is
    "mps", and the given length is 6, return "fox ju". The first occurence of "mps" is right
    after the size characters 'f', 'o', 'x', ' ', 'j', and 'u'.
    """
    pass


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

test_n_chars_before_pattern = TstRunner(test_cases=test_cases,
                                        arg_extractor=lambda case: [case['text'], case['pattern'], case['n']])
