class Solution:
    def __init__(self):
        self.Dic ={ '1', '2', '3', '4', '5',
                        '6', '7', '8', '9', '10',
                        '11','12','13','14','15',
                        '16','17','18','19','20',
                        '21','22','23','24','25',
                        '26'}

    '''
     1         1           1           1           1
     A        AA        AAA     AAAA       AAAAA
               |K          KA       KAA         KAAA
                            |AK      AKA         AKAA
                                       |AAK        AAKA
                                       |KK          KKA
                                                      |AAAK
                                                      |KAK
                                                      |AKK
    '''

    def numDecodings(self, s: str) :
        if(len(s) == 0):
             return 0          
        DP = [0] * len(s)
        for i in range(len(s)):
            if(i == 0):
                if(s[i] in self.Dic):
                    DP[0] = 1
                else:
                    DP[0] = 0
                    
            elif(i == 1):
                if(s[i] in self.Dic):
                    DP[1] = DP[0]
                if(s[0:2] in self.Dic):
                    DP[1] += 1

            else:
                 # find s[:i] + s[i]
                if(s[i] in self.Dic):
                    DP[i] = DP[i-1]
                # find s[:i-1] + s[i-1:i+1]
                if(s[i-1:i+1] in self.Dic):
                    DP[i] += DP[i-2]
            print(DP)
        return DP[-1]

s = "10"
sol = Solution()
print(sol.numDecodings(s))
            
                
