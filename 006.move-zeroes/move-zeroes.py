from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while i != len(nums):
            if nums[j] == 0:
                del nums[j]
                nums.append(0)
            if nums[j] != 0:
                j += 1
            i += 1


nums = [0, 0, 1]
Solution().moveZeroes(nums)
print(nums)
