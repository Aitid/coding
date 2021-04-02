from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    left = 0
    right = 0
    s = 0
    zero = 0
    mx = 0
    while right < len(nums):
        if nums[right] == 0:
            zero += 1
        while zero == 2:
            if nums[left] == 0:
                zero -= 1
            left += 1
        s = right - left + 1
        mx = max(mx, s)
        right += 1
    return mx


if __name__ == '__main__':
    assert findMaxConsecutiveOnes([1, 0, 1, 1, 0, 0, 1, 1]) == 4
    assert findMaxConsecutiveOnes([0, 0]) == 1
    assert findMaxConsecutiveOnes([0]) == 1
