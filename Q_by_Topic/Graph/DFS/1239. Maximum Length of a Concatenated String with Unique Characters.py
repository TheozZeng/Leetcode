class Solution:
    def __init__(self):
        self.arr = []
        self.Proccessed = set()
        self.res = -float("inf")
        return 

    # char_have = set of char already added
    #char_left list of index in self.arr not added
    def DFS(self, char_have, char_left):
        if(char_have in self.Proccessed):
            return
        self.res = max(self.res, len(char_have))
        print(char_have,":",char_left)
        self.Proccessed.add(char_have)
        char_have = set(char_have)
        for index in char_left:
            new = self.arr[index]
            num_common = len(char_have.intersection(new))
            if(num_common == 0):
                new_char_have = list(char_have) + list(new)
                new_char_have.sort()
                new_s = "".join(new_char_have)
                new_char_left = char_left[:]
                new_char_left.remove(index)
                self.DFS(new_s,new_char_left)
        
        return
        
    def maxLength(self, arr):
        index = 0
        char_left = []
        for s in arr:
            if(len(s) == len(set(s))):
                self.arr.append(set(s))
                char_left.append(index)
                index += 1
        print(self.arr)

        self.DFS("",char_left)
        return self.res




arr = ["yy","bkhwmpbiisbldzknpm"]
sol =  Solution()
print(sol.maxLength(arr))

