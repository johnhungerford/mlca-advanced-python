from typing import List, Tuple
from algorithms.dicts.two_sum import test_two_sum

# Copy this function
def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Find two elements in a list of integers (nums) that add up to given target integer (target).
    Assume that there will only be one pair of integers that adds up to the target. Return the
    indices of the two elements in any order.
    """
    for i in List:
        for j in list:
            if i+j==target:
                return i,j
    

test_two_sum.run_on(two_sum)
