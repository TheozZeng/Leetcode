class Solution:
    def count_Substring_with_center(self,s,i):
        count = 0
        # aba
        l = i
        r = i
        while(0<= l and r<len(s)):
            if(s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            else:
                break

        #abba
        l = i
        r = i + 1
        while(0<= l and r<len(s)):
            if(s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            else:
                break
        return count
            
        
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.count_Substring_with_center(s,i)
        return count

s = "aaa"
sol = Solution()
print(sol.countSubstrings(s))
