from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            print(i)
        return len(nums)

solution = Solution()
nums = [1, 3, 4, 5, 6]
target = 6
output = solution.searchInsert(nums, target)

print("Output:", output)
