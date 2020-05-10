class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        if(length ==0):
            return 0
        for i, char in enumerate(haystack):
            print(i, char, end="|")
            print(haystack[i:i+length])
            if(haystack[i:i+length] == needle):
                return i
        return -1



haystack = ""
needle = ""
sol = Solution()
print(sol.strStr(haystack,needle))
