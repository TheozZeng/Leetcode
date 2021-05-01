class Solution:
    def __init__(self):
        self.s1 = ""
        self.s2 = ""
        self.s3 = ""
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.already_processed = set()
        self.res = False
        
    def extract_char(self,i,j,k):
        if((i,j,k) in self.already_processed):
            return
        self.already_processed.add((i,j,k))
        print(i,"-",j,"-",k)
        if(self.res == True):
            return
        if(i == self.n1):
            if(self.s2[j:] == self.s3[k:]):
                self.res = True
            return
        
        if(j == self.n2):
            if(self.s1[i:] == self.s3[k:]):
                self.res = True
            return

        if(k == self.n3):
            if(i == self.n1 and j == self.n2):
                self.res = True
            return

        char1 = self.s1[i]
        char2 = self.s2[j]
        char3 = self.s3[k]
        if(char1 == char3 and char2 == char3):
            self.extract_char(i+1,j,k+1)
            self.extract_char(i,j+1,k+1)
        elif(char1 == char3):
            self.extract_char(i+1,j,k+1)
        elif(char2 == char3):
            self.extract_char(i,j+1,k+1)
        return
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.n1 = len(s1)
        self.n2 = len(s2)
        self.n3 = len(s3)
        if(abs(self.n1 - self.n2) > 1):
            return False
        self.extract_char(0,0,0)
        return self.res

s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
sol = Solution()
print(sol.isInterleave(s1,s2,s3))
        
