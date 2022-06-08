from re import L
from typing import List

from algorithms.lists.find_value_index import test_find_value_index


def find_value_index(nums: List[int], target: int) -> int:
    """This function searches a *sorted* list of numbers (ascending order) for a
       target value. If it finds the value it returns its index. If it does not
       find the value, it returns the index where that value would be if it were in the list"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    for i in range(len(List)):
        if List[i] == target:
            return i
        elif List[i] < target and List[i+1] > target:
            return i+1
            
=======
=======
>>>>>>> 42284cd85e21cf0a866b17ad88f37c9bdf5091f5
=======
>>>>>>> 42284cd85e21cf0a866b17ad88f37c9bdf5091f5
    for i in range(0, len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 42284cd85e21cf0a866b17ad88f37c9bdf5091f5
=======
>>>>>>> 42284cd85e21cf0a866b17ad88f37c9bdf5091f5
=======
>>>>>>> 42284cd85e21cf0a866b17ad88f37c9bdf5091f5


test_find_value_index.run_on(find_value_index)
