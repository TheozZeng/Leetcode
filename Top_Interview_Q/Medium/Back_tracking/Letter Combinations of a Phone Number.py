class Solution:
    def __init__(self):
        self.L = []
        self.M = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],
                      "6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        
    def back_tracking(self, digits, string):
        if(len(digits)==0):
            self.L.append(string)
            return
            
        l = self.M[digits[0]]
        for char in l:
            self.back_tracking(digits[1:], string + char)
            
        
    def letterCombinations(self, digits: str):
        if(len(digits)==0):
            return []
        self.back_tracking(digits, "")
        return self.L


digits = "23"
sol = Solution()
print(sol.letterCombinations(digits))
