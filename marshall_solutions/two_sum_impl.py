from typing import List, Tuple
from algorithms.dicts.two_sum import test_two_sum

# Copy this function
def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Find two elements in a list of integers (nums) that add up to given target integer (target).
    Assume that there will only be one pair of integers that adds up to the target. Return the
    indices of the two elements in any order.
    """

    nums_dict = {}
    for idx in range(len(nums)):
        nums_dict[nums[idx]] = idx

    for n in nums:
        if target - n in nums_dict:
            return n, nums_dict[target - n]
    

test_two_sum.run_on(two_sum)

