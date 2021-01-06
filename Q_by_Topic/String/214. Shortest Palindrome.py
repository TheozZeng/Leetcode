class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s1 = s[::-1]
        i = 0
        j = len(s)
        while(s1[i:] != s[:j]):
            print(s1[i:] ,"----",s[:j])
            i+= 1
            j -= 1
        return s1[:i] + s


s = "abcdef"
sol = Solution()
print(sol.shortestPalindrome(s))
        
        
