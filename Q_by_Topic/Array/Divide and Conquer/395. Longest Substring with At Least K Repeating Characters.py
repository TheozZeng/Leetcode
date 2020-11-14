class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if(len(s) < k):
            return 0
        
        Dic = {}
        for char in s:
            if(char in Dic):
                Dic[char] += 1
            else:
                Dic[char] = 1
        for char in Dic:
            if(Dic[char] < k):
                # break at char
                break_index = s.index(char)
                s1 = s[:break_index]
                s2 = s[break_index+1:]
                return max(self.longestSubstring(s1,k), self.longestSubstring(s2,k))
        return len(s)
        
