class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxlength , start = 0 , 0
        seen = {}
        
        for i in range(len(s)):
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]] + 1
            else:
                maxlength = max(maxlength , i - start + 1)
            seen[s[i]] = i
            
        return maxlength

s = "abba"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
