class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        print("setelah dirapikan:", s.strip())

        if not s:
            return 0
        
        last_space_index = s.rfind(' ')
    
        if last_space_index == -1:
            return len(s)
    
        return len(s) - last_space_index - 1

solution = Solution()    
s = "     Wingardium Leviosa"
panjang_kata_terakhir = solution.lengthOfLastWord(s)
print("sebelum dirapikan:", s)
print(panjang_kata_terakhir)
