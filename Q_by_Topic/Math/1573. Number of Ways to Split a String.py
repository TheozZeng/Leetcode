class Solution:
    def all_0(self,n):
        if(n < 3):
            return 0
        #level 1
        L1 = []
        for i in range(2,n):
            L1.append(i)
        print(L1)
        #level 2
        num = 0
        for count in L1:
            for i in range(1,count):
                num += 1
        return num
        
    def numWays(self, s: str) -> int:
        n_1 = s.count("1")

        # no 1
        if(n_1 == 0):
            return self.all_0(len(s))


        # have 1
        if(n_1 % 3 != 0):
            return 0 

        count =  n_1//3
        n0_1 = 0
        n0_2 = 0
        part = 1
        part2 = ""
        part3 = ""

        # get sub part
        for c in s:
            if(count == 0):
                count =  n_1//3
                part += 1
                
            if(part == 1):
                if(c == "1"):
                    count -= 1
                
            if(part == 2):
                if(c == "1"):
                    count -= 1
                part2 += c
                
            if(part == 3):
                if(c == "1"):
                    count -= 1
                part3 += c

        #count leading 0 in part2/part3
        n2 = 0
        for c in part2:
            if(c == "0"):
                n2 += 1
            else:
                break
        
        n3 = 0
        for c in part3:
            if(c == "0"):
                n3 += 1
            else:
                break
                
        return (n2+1)*(n3 + 1)


s = "0000"
sol = Solution()
print(sol.numWays(s))
        
