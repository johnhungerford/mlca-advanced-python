from re import L
from typing import List

from algorithms.lists.find_value_index import test_find_value_index


def find_value_index(nums: List[int], target: int) -> int:
    """This function searches a *sorted* list of numbers (ascending order) for a
       target value. If it finds the value it returns its index. If it does not
       find the value, it returns the index where that value would be if it were in the list"""
    for i in range(0, len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)


test_find_value_index.run_on(find_value_index)
