# DFS & memorization 
class Solution:
    def __init__(self):
        self.found = False
        #memorize part of string left to be composed
        self.S = set()
        
    def Search(self, s, wordDict):
        '''
        print("___________________")
        print(s)
        '''
        
        if(len(s)== 0):
            self.found = True
            return
        
        if(self.found):
            return
        
        if(s in self.S):
            return
        else:
            self.S.add(s)
        
            
        for word in wordDict:
            w_len = len(word)
            if(w_len > len(s)):
                continue

            #print(word,"|",s[0:w_len])
            if(s[0:w_len] == word):
                self.Search(s[w_len:],wordDict)
        
                
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict[:] = sorted(wordDict, key=len)
        self.Search(s,wordDict[::-1])
        return self.found

    
s = "abcd"
wordDict = ["a","abc","b","cd"]
sol = Solution()
print(sol.wordBreak(s,wordDict))
        
