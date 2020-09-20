class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0: return "1"
        if n == 1: return "1"
        prev = self.countAndSay(n-1)
        cnt = 0 
        s = ""
        for i in range(len(prev)):
            cnt += 1
            # i is the last char OR not same as before
            if i == len(prev) - 1 or prev[i] != prev[i+1]:
                s += str(cnt) + prev[i]
                cnt = 0
        return s
                


        