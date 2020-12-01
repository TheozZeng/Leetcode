class Solution:
    def __init__(self):
        self.Dic ={ '1':'A', '2':'B', '3':'B', '4':'C', '5':'E',
                        '6':'F', '7':'G', '8':'H', '9':'I','10':'J',
                        '11':'K','12':'L','13':'M','14':'N','15':'O',
                        '16':'P','17':'Q','18':'R','19':'S','20':'T',
                        '21':'U','22':'V','23':'W','24':'X','25':'Y',
                        '26':'Z'}
        self.S = set()
        self.res = set()
        
    def Back_track(self,s):
        print(s)
        # check sequence processed
        if(s in self.S or s == None):
            return
        self.S.add(s)
        # generate next sequence
        res1 = None
        res2 = None
        finish = True
        for i in range(len(s)):
            if(s[i].isdigit()):
                if(i == len(s)-1):
                    if(s[i] != "0"):
                        res1 = s[:i] + self.Dic[s[i]]
                    res2 = None
                    
                elif(i == len(s)-2):
                    if(s[i] != "0"):
                        res1 = s[:i] + self.Dic[s[i]] + s[i+1:]
                    if(s[i:i+2] in self.Dic):
                        res2 = s[:i] + self. Dic[s[i:i+2]]
                    else:
                        res2 = None
                        
                else:
                    if(s[i] != "0"):
                        res1 = s[:i] + self.Dic[s[i]] + s[i+1:]
                    if(s[i:i+2] in self.Dic):
                        res2 = s[:i] + self. Dic[s[i:i+2]] + s[i+2:]
                    else:
                        res2 = None
                finish = False
                break
                    
        if(finish):
            self.res.add(s)
            return
        
        #back track
        self.Back_track(res1)
        self.Back_track(res2)
                
            
                
        
    def numDecodings(self, s: str) -> int:
        self.Back_track(s)
        return len(self.res)

s = "11111"        
sol =  Solution()
print(sol.numDecodings(s))
