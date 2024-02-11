class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Menginisialisasi index1 dan index2 dengan -1
        index1 = -1
        index2 = -1

        # Mencari indeks karakter pertama dari kata terakhir
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                index1 = i
                break

        # Mencari indeks karakter terakhir dari kata terakhir
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                index2 = i
                break

        # Jika tidak ada kata yang ditemukan, kembalikan 0
        if index1 == -1 or index2 == -1:
            return 0

        # Mengembalikan panjang kata terakhir
        return index2 - index1 + 1

# Membuat instance dari kelas Solution
sol = Solution()

# Contoh penggunaan
s = "Hello World"
print(sol.lengthOfLastWord(s))  # Output yang diharapkan: 5
