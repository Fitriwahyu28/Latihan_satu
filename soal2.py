from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            else:
                j = i + 1
        return j

# Contoh penggunaan
sol = Solution()
nums = [1, 3, 5, 6]
target = 5
print(sol.searchInsert(nums, target))  # Output yang diharapkan: 2
