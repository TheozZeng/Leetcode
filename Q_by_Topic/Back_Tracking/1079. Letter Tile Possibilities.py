class Solution:
    def __init__(self):
        self.res = -1
        
    def Back_track(self, s, D):
        self.res += 1
        print(self.res,"|", s, "|",D)
        for key in D:
            D_new = D.copy()
            D_new[key] -= 1
            s_new = s + key
            if(D_new[key] <= 0):
                del D_new[key]
            self.Back_track(s_new,D_new)
            
    def numTilePossibilities(self, tiles: str) -> int:
        D = {}
        for c in tiles:
            if(c in D):
                D[c] += 1
            else:
                D[c] = 1
        print(D)
        self.Back_track("",D)

tiles = "AAABBC"
sol = Solution()
print(sol.numTilePossibilities(tiles))
        
