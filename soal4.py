class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# Membuat instance dari kelas Solution
sol = Solution()

# Memanggil fungsi climbStairs dan mencetak hasilnya
print(sol.climbStairs(4))  # Ganti 5 dengan angka yang Anda inginkan
