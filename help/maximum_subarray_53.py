from typing import List
from math import inf


def maxSubArray(nums: List[int]) -> int:
    """
    O(n^2)
    """
    mx = -inf
    for i in range(len(nums)):
        curr = 0
        for j in range(i, len(nums)):
            curr += nums[j]
            mx = max(curr, mx)
    return mx

def maxSubArray(self, nums: List[int]) -> int:
    """
    O(n)
    """
    mx = -inf
    sub = 0
    i = 0
    while i < len(nums):
        sub += nums[i]
        mx = max(mx, sub)
        if sub < 0:
            sub = 0
        i += 1
    return mx

if __name__ == '__main__':
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5,4,-1,7,8]) == 23

