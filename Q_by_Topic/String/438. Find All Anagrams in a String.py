class Solution:
    def gen_dic(self, sub_s):
        dic = {}
        for c in sub_s:
            if(c in dic):
                dic[c] += 1
            else:
                dic[c] = 1
        return dic
    
    def findAnagrams(self, s: str, p: str):
        
        l = len(p)
        res = []
        tar = self.gen_dic(p)
        this = {}
        
        for i in range(len(s) - l + 1):
            if(i == 0):
                this = self.gen_dic(s[i:i+l])
            else:
                prev_char = s[i-1]
                this[prev_char] -= 1
                if(this[prev_char] == 0):
                    this.pop(prev_char)
                    
                new_char = s[i+l-1]
                if(new_char in this):
                    this[new_char] += 1
                else:
                    this[new_char] = 1
            print(s[i:i+l],":",this)
            if(tar == this):
                res.append(i)
                
                
        return res
            
        

sol = Solution()
s =  "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s,p))
