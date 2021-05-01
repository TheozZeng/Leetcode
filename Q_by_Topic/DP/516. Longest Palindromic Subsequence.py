class Solution:
    def print_DP(self,DP):
        for row in DP:
            print(row)
        print("--------------------------")
        
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        a                i==j   DP[i][j] = 1
        a*****a       s[i]==s[j]   DP[i][j] = DP[i+1][j-1] + 2
        a*****b       s[i] != s[j]  DP[i][j] = max(DP[i+1][j] , DP[i][j-1])
        '''
        n = len(s)
        DP = []
        for r in range(n):
            row = [0]*n
            DP.append(row)

        # l = len(substr)
        for l in range(n):
            for i in range(n-l):
                j = i+l
                if(i == j):
                    DP[i][j] = 1
                    continue
                if(s[i] == s[j]):
                    DP[i][j] = DP[i+1][j-1] + 2
                else:
                    DP[i][j] = max(DP[i+1][j],DP[i][j-1])
            self.print_DP(DP)
            
        return DP[0][n-1]





s = "bbbab" 
sol = Solution()
print(sol.longestPalindromeSubseq(s))
