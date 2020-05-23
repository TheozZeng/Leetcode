class Solution:
    def trailingZeroes(self, n: int) -> int:
        flag = True
        count = 0
        power = 1
        
        while(flag):
            x = n//(5**power)
            count += x
            power += 1
            if(x == 0):
                break
        return count
            
        
