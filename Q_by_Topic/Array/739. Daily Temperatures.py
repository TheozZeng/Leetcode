class Solution:
    def dailyTemperatures(self, T):
        Dic = {}
        res = len(T) * [0]
        
        # use Dic store previous day t:day that haven't found next day
        for i in range(len(T)):
            now_t = T[i]
            
            for prev_t in Dic:
                if(prev_t < now_t):
                    prev_day_list = Dic[prev_t]
                    for prev_day in prev_day_list:
                        day_diff = i - prev_day
                        res[prev_day] = day_diff
                    Dic[prev_t] = []


            # add today to Dic that haven't found next day
            if(now_t in Dic):
                Dic[now_t].append(i)
            else:
                Dic[now_t] = [i]
        
        return res
                
                    
                        







T = [73, 74, 75, 71, 69, 72, 76, 73]
sol = Solution()
print(sol.dailyTemperatures(T))
