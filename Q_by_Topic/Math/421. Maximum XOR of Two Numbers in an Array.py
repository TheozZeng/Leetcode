class Solution:
    def __init__(self):
        self.D = {"0":"1", "1":"0"}
        self.max_len = 0
        self.nums = []
        self.res = -float("inf")

    def init_binary(self):
        max_num = max(self.nums)
        max_len = len(bin(max_num)[2:])
        self.max_len = max_len
        
        for i in range(len(self.nums)):
            n = self.nums[i]
            n = bin(n)[2:]
            l_n = len(n)
            n = (max_len - l_n)*"0" + n
            self.nums[i] = n

    def find_max_Xor(self, i, res , L):
        #print(i,":",res,":",L)

        if(len(L) == 1):
            res = int(res,base = 2) ^ int(L[0],base=2)
            print("->",res)
            self.res = max(self.res,res)
            return           
            
        char_i = res[i]
        char_need = self.D[char_i]
        newL = []
        for n in L:
            if(n[i] == char_need):
                newL.append(n)
        if(len(newL) > 0):
            self.find_max_Xor(i+1,res,newL)
        else:
            self.find_max_Xor(i+1,res,L)
        
                
            
            
    def findMaximumXOR(self, nums):
        if(len(nums) <= 1):
            return 0
        self.nums = nums
        self.init_binary()
        for i in self.nums:
            if(i[0] == "1"):
                self.find_max_Xor(0,i,self.nums)
        return self.res



nums = [4,6,7]
sol = Solution()
print(sol.findMaximumXOR(nums))
