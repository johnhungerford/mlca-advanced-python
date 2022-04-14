from typing import List, Tuple
from algorithms.dicts.two_sum import test_two_sum

# Copy this function
def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Find two elements in a list of integers (nums) that add up to given target integer (target).
    Assume that there will only be one pair of integers that adds up to the target. Return the
    indices of the two elements in any order.
    """
    # return None, None
    for i, i_val in enumerate(nums):
        for j in range(i + 1, len(nums)):
            j_val = nums[j]
            if i != j:
                if i_val + j_val == target:
                    return i, j

test_two_sum.run_on(two_sum)