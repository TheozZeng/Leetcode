class Solution:
    def validUtf8(self, data):
        L = [
             (0b10000000,0b00000000), # 1 byte
             (0b11100000,0b11000000), # 2 byte
             (0b11110000,0b11100000), # 3 byte
             (0b11111000,0b11110000) # 4 byte
            ]
        
        count = 0
        for num in data:
            print(hex(num & 0xFF))
            if(count == 0):
                count = None
                for i in range(0,len(L)):
                    mask = L[i][0]
                    tar = L[i][1]
                    print(i,hex(num & mask), num & mask == tar)
                    if(num & mask == tar):
                        count = i
                        break
                if(count == None):
                    return False
            else:
                mask = 0b11000000
                tar = 0b10000000
                if(num & mask == tar):
                    count -= 1
                else:
                    return False
        if(count != 0):
            return False
        return True


data = [237]
sol = Solution()
print(sol.validUtf8(data))
