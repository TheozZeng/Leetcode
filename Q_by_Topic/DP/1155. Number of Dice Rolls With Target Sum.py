class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) :
        prev_level = {0:1}
        while(d>0):
            this_level = {}
            for s in prev_level:
                prev_count = prev_level[s]
                for i in range(1,f+1):
                    new_sum = s+i
                    if(new_sum in this_level):
                        this_level[new_sum] += prev_count
                    else:
                        this_level[new_sum] = prev_count
            print(this_level)
            prev_level =   this_level
            d -= 1
        if(target in prev_level):
            return prev_level[target]
        return 0
             



d = 2
f = 6
target = 7
sol = Solution()
sol.numRollsToTarget(d,f,target)
        
