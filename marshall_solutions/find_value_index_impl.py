from typing import List

from algorithms.lists.find_value_index import test_find_value_index


def find_value_index(nums: List[int], target: int) -> int:
    """This function searches a *sorted* list of numbers (ascending order) for a
       target value. If it finds the value it returns its index. If it does not
       find the value, it returns the index where that value would be if it were in the list"""

    if target > nums[-1]:
        return len(nums) +  target - nums[-1]

    elif target < nums[0]:
        return target - nums[0] 

    else:
        for idx in range(len(nums) - 1):
            if nums[idx] == target:
                return idx
        


test_find_value_index.run_on(find_value_index)
