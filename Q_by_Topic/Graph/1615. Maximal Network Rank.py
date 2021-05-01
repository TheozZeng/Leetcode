class Solution:
    def __init__(self):
        self.Dic = {}
        return
    
    def init_Dic(self,roads):
        for road in roads:
            pos1 = min(road[0],road[1])
            pos2 = max(road[0],road[1])
            if pos1 not in self.Dic:
                self.Dic[pos1] = set()
                self.Dic[pos1].add((pos1,pos2))
            else:
                self.Dic[pos1].add((pos1,pos2))
            if pos2 not in self.Dic:
                self.Dic[pos2] = set()
                self.Dic[pos2].add((pos1,pos2))
            else:
                self.Dic[pos2].add((pos1,pos2))
        return
    
    def print_dic(self):
        for pos in self.Dic:
            print(pos,":",self.Dic[pos])
            
    def maximalNetworkRank(self, n: int, roads):
        self.init_Dic(roads)
        self.print_dic()

        Max1 = [0,[]] #size, [pos1,pos2...]
        Max2 = [0,[]]
        
        for pos in self.Dic:
            size = len(self.Dic[pos])
            if size > Max1[0]:
                Max2 = Max1
                Max1 = [size,[pos]]
            elif size == Max1[0]:
                Max1[1].append(pos)
            else:
                if size > Max2[0]:
                    Max2 = [size,[pos]]
                elif size == Max2[0]:
                    Max2[1].append(pos)
        print(Max1)
        print(Max2)

        res = 0
        L1 = Max1[1]
        if(len(L1) > 1):
            for i in range(len(L1)):
                for j in range(i+1,len(L1)):
                    pos1 = L1[i]
                    pos2 = L1[j]
                    set1 = self.Dic[pos1]
                    set2 = self.Dic[pos2]
                    res = max(res, len(set1.union(set2)))
                    
        elif(len(L1) == 1):
            pos1 = L1[0]
            set1 = self.Dic[pos1]
            L2 = Max2[1]
            for pos2 in L2:
                set2 = self.Dic[pos2]
                res = max(res, len(set1.union(set2)))
            
        return res

n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
sol = Solution()
print(sol.maximalNetworkRank(n, roads))
        
        
        
