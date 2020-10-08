class Solution:
    def partitionLabels(self, S: str):
        Dic = {}
        for i in range(len(S)):
            char = S[i]
            if char in Dic:
                pos = Dic[char]
                start = pos[0]
                end = pos[1]
                start = min(start,i)
                end = max(end,i)
                Dic[char] = [start,end]
            else:
                Dic[char] = [i,i]

        dictlist = []
        for key, value in Dic.items():
            temp = [key,value]
            dictlist.append(temp)
        dictlist.sort(key=lambda k: k[1][0])
        #print(dictlist)

        L = []
        for info in dictlist:
            start = info[1][0]
            end = info[1][1]

            if(len(L)==0):
                L.append([start,end])
            else:
                now_range = L.pop()
                now_start = now_range[0]
                now_end = now_range[1]
                if(start <= now_end):
                    now_start = min(now_start,start)
                    now_end = max(now_end,end)
                    L.append([now_start,now_end])
                else:
                    L.append([now_start,now_end])
                    L.append([start,end])
        res = []
        for Range in L:
            res.append(Range[1]-Range[0]+1)
        return res


sol = Solution()

S = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(S))
