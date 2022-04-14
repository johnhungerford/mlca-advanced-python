from ast import Call
import time
from typing import Callable, Any, List, Optional

from colorama import init, deinit

class TestRunnerException(Exception):
    pass


class TestRunner:
    """A class for testing functions using test data"""

    __run_all: bool = True

    def __init__(self,
                 test_cases: Optional[List[dict[str, Any]]] = None,
                 evaluator: Optional[Callable[[Any, Any], bool]] = None,
                 arg_extractor: Optional[Callable[[dict[str, Any]], Any]] = None,
                 fn: Optional[Callable] = None):

        self.__test_cases = test_cases
        if evaluator is None:
            self.__evaluate_results = lambda a, e: a == e
        else:
            self.__evaluate_results = evaluator

        self.__extract_args = arg_extractor
        self.__target_fn = fn

    def add_test(self, test_case: dict[str, Any]) -> 'TestRunner':
        self.__test_cases.append(test_case)
        return self
    
    def add_tests(self, test_cases: List[dict[str, Any]]) -> 'TestRunner':
        self.__test_cases.extend(test_cases)
        return self
    
    def clear_tests(self) -> 'TestRunner':
        self.__test_cases = []
        return self
    
    def use_extractor(self, extractor: Callable[[dict[str, Any]], Any]) -> 'TestRunner':
        self.__extract_args = extractor
        return self
    
    def clear_extractor(self) -> 'TestRunner':
        self.__extract_args = None
        return self
    
    def target_function(self, fn: Callable) -> 'TestRunner':
        self.__target_fn = fn
        return self
    
    def clear_target_fn(self) -> 'TestRunner':
        self.__target_fn = None
        return self

    def use_evaluator(self, evaluator: Callable[[Any, Any], bool]) -> 'TestRunner':
        self.__evaluate_results = evaluator
        return self

    def clear_evaluator(self) -> 'TestRunner':
        self.__evaluate_results = None
        return self

    def run_tests(self) -> None:
        if self.__test_cases is None or self.__evaluate_results is None or self.__run_impl is None:
            raise TestRunnerException('test_cases, evaluator, and runner must be defined to run tests')
        
        self.__run_tests(self.__test_cases, self.__evaluate_results, self.__run_impl)

    def run_on(self, target_fn: Callable) -> None:
        self.__run_tests(self.__test_cases, self.__evaluate_results, self.__extract_args, target_fn)

    def __run_tests(self,
                    test_cases: List[dict[str, Any]],
                    evaluator: Callable[[Any, Any], bool],
                    extractor: Callable[[dict[str, Any]], Any],
                    target_fn: Callable) -> None:
        if test_cases is None or evaluator is None or extractor is None or target_fn is None:
            msgs = []
            if test_cases is None:
                msgs.append('test_cases is None')
            if evaluator is None:
                msgs.append('evaluator is None')
            if extractor is None:
                msgs.append('extractor is None')
            if target_fn is None:
                msgs.append('target function is None')
            raise TestRunnerException('test cases, evaluator, extractor, and target function must be defined to run tests: ' + '; '.join(msgs))

        init()
        i = 1
        print('\n  *****************\n  * Running Tests *\n  *****************\n')
        for case in self.__test_cases:
            start_time = time.time()

            try:
                expected = case['expected']
                args = extractor(case)
                actual = target_fn(*args)
                passed = evaluator(actual, expected)
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
                print(f'  {i}: \033[1;32mPassed!\033[0m ({time_elapsed_ms} milliseconds)')
            else:
                print(f'  {i}: \033[1;31mFailed!\033[0m\n')
                for msg_line in msg:
                    print(f'      {msg_line}')
                print('')
                if not self.__run_all:
                    deinit()
                    return

            i += 1

        deinit()
        print('')
