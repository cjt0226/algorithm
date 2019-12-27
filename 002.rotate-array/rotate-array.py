from typing import List


class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     kr = k % len(nums)
    #     nums_r = nums[:-kr]
    #     nums_l = nums[-kr:]
    #     nums.clear()
    #     nums.extend(nums_l)
    #     nums.extend(nums_r)

    # def rotate(self, nums: List[int], k: int) -> None:
    #     nl = len(nums)
    #     if k > 0 and k % nl:
    #         kr = k % nl
    #         nums.extend(nums[-kr:])
    #         nums.extend(nums[:nl - kr])
    #         del nums[:nl]

    # def rotate(self, nums: List[int], k: int) -> None:
    #     for i in range(k):
    #         nums.insert(0, nums.pop())

    def rotate(self, nums: List[int], k: int) -> None:
        nl = len(nums)
        if k > 0 and k % nl:
            kr = k % nl
            nums[:] = nums[-kr:] + nums[:nl - kr]



nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums)
