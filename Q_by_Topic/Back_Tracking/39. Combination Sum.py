class Solution:
    def __init__(self):
        self.res = set()
        
    def back_tracking(self,candidates,target, L):
        if(target <0):
            return
        if(target == 0):
            L.sort()
            self.res.add(tuple(L))
        else:
            for i in candidates:
                new_L = L[:]
                new_L.append(i)
                self.back_tracking(candidates,target - i, new_L)
            
    def combinationSum(self, candidates, target):
        self.back_tracking(candidates,target, [])
        L =[]
        for comb in self.res:
            L.append(list(comb))
        return L

sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates, target))
