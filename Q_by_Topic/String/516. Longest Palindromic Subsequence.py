class Solution:
    def is_palidrom(self,s):
        i = 0
        j = len(s)-1
        while(i <= j):
            if(s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True
    
    def longestPalindromeSubseq(self, s: str) -> int:
        L = set()
        L.add("")
        
        for c in s:
            additional_string = set()
            for string in L:
                new_string = string + c
                additional_string.add(new_string)
            L = L.union(additional_string)

        L = sorted(L, key=len, reverse=True)
        for sub_s in L:
            if(self.is_palidrom(sub_s)):
                print(sub_s)
                return len(sub_s)

sol = Solution()
print(sol.longestPalindromeSubseq("bbbab"))
