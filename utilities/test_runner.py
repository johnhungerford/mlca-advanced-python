import abc
import time


class TestRunner(abc.ABC):
    """A class for testing functions using test data"""

    def __init__(self, test_cases: list):
        for case in test_cases:
            assert('expected' in case)

        self.__test_cases: list = test_cases

    @abc.abstractmethod
    def run_function(self, test_case: dict):
        """Run the function being tested with data extracted from a test case"""
        pass

    def compare_result(self, actual, expected) -> bool:
        """Determine if test has passed or failed based on actual result and the
           expected value defined in the test case"""
        return actual == expected

    def run_tests(self) -> None:
        i = 1
        print('\n  *****************\n  * Running Tests *\n  *****************\n')
        for case in self.__test_cases:
            start_time = time.time()

            try:
                expected = case['expected']
                actual = self.run_function(case)
                passed = self.compare_result(actual, expected)
                if not passed:
                    msg = [f'Expected', '========', str(expected), '', 'Actual', '======', str(actual)]
                else:
                    msg = []

            except Exception as e:
                passed = False
                msg = [f'Raised {type(e).__name__}:', str(e)]

            end_time = time.time()
            time_elapsed_ms = (end_time - start_time) * 1000

            if passed:
                print(f'  {i}: \033[1;32m Passed!\033[0m ({time_elapsed_ms} milliseconds)')
            else:
                print(f'  {i}: \033[1;31m Failed!\033[0m\n')
                for msg_line in msg:
                    print(f'      {msg_line}')
                print('')

            i += 1
