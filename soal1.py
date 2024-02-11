from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

# Contoh penggunaan
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    result_length = sol.removeElement(nums, val)
    print(result_length)  # Panjang array setelah menghapus elemen 3
    print(nums[:result_length])  # Elemen-elemen array setelah menghapus elemen 3
