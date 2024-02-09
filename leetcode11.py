class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Inisialisasi array untuk menyimpan jumlah cara untuk setiap langkah
        dp = [0] * (n + 1)
        dp[1] = 1  # Jika hanya ada satu tangga, hanya ada satu cara
        dp[2] = 2  # Jika ada dua tangga, ada dua cara (1+1 atau 2)
        
        # Menghitung jumlah cara untuk setiap langkah
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# Contoh penggunaan
solution = Solution()
n = 2
output = solution.climbStairs(n)
print("Output:", output)
