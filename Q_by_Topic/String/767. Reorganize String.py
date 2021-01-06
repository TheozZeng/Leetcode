class Solution:
    def reorganizeString(self, S: str) -> str:
        D = {}
        for c in S:
            if(c not in D):
                D[c] = 1
            else:
                D[c] += 1

        print(D)

        D = sorted(D.items(), key=lambda item: item[1],reverse = True)
        print(D)


        count = D[0][1]
        index  = 0
        res = [""]*count
        
        for char in D:
            c = char[0]
            n = char[1]
            for i in range(n):
                res[index]  += c
                index += 1
                if(index == count):
                    index = 0
                
                    
        print(res)            
        res_s = "|"
        for s in res:
            last_c = res_s[-1]
            if(last_c == s[0]):
                return ""
            else:
                res_s += s
                
        return res_s[1:]


S = "vvvlo"
sol = Solution()
print(sol.reorganizeString(S))
            
        
