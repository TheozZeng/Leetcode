class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        max_str = ""
        for i in range(0,len(s)):
            this_len = 1
            this_str = ""
            l = i
            r = i
            # aba----------------------
            while(l >= 0 and r < len(s)):
                if(s[l] == s[r]):
                    l -= 1
                    r += 1
                else:
                    break
            if(this_len < r-l+1):
                this_len = r-l+1
                this_str = s[l+1:r]
            #abba----------------------
            l = i
            r = i+1
            while(l >= 0 and r < len(s)):
                if(s[l] == s[r]):
                    l -= 1
                    r += 1
                else:
                    break
            if(this_len < r-l+1):
                this_len = r-l+1
                this_str = s[l+1:r]
            #---------------------------
            if(max_len < this_len):
                max_len = this_len
                max_str = this_str
        return max_str

s = "babaddd"
sol = Solution()
print(sol.longestPalindrome(s))
                
                
            
                    
            
