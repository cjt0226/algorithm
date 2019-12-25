from typing import List


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     index = 0
    #     length = len(nums) - 1
    #     while index < length:
    #         if nums[index] == nums[index + 1]:
    #             nums.pop(index)
    #             length -= 1
    #         else:
    #             index += 1
    #     return len(nums)
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for value in sorted(list(set(nums))):
            nums[index] = value
            index += 1
        del nums[index:]
        return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums_len = Solution().removeDuplicates(nums)
print(nums_len)

for i in range(nums_len):
    print(nums[i])
