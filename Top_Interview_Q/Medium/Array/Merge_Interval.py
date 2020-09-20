class Solution:
    def merge(self, intervals):
        intervals.sort(key = operator.itemgetter(0))
        res = []
        for interval in intervals:
            if(len(res) == 0):
                res.append(interval)
            else:
                last_interval = res[-1]
                last_l = last_interval[0]
                last_r = last_interval[1]
                l = interval[0]
                r = interval[1]
                if(last_l <= l <= last_r):
                    res.pop()
                    new_l = min(l,last_l)
                    new_r = max(r,last_r)
                    res.append([new_l,new_r])
                else:
                    res.append(interval)
        return res