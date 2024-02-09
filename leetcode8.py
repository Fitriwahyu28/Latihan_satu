from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
  

solution = Solution()  
nums = [4,6,7,7,4,]
val = 7
index = solution.removeElement(nums, val)
print("Panjang baru:", index)
print("Daftar setelah menghapus nilai", val, ":", nums[:index])