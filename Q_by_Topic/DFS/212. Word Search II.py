class Solution:
    def __init__(self):
        self.board = None
        self.n_r = 0
        self.n_c = 0
        self.res = []
        
    def DFS(self, r,c, used_block, words, original_word):
        if(original_word in self.res):
            return
        if(len(words) == 0):
            self.res.append(original_word)
            return
        if(r<0 or c<0 or r>= self.n_r or c>=self.n_c):
            return
        if((r,c) in used_block):
            return
        char = self.board[r][c]
        if(char == words[0]):
            new_used_block = used_block.copy()
            new_used_block.add((r,c))
            self.DFS(r-1,c, new_used_block, words[1:], original_word)
            self.DFS(r,c-1, new_used_block, words[1:], original_word)
            self.DFS(r+1,c, new_used_block, words[1:], original_word)
            self.DFS(r,c+1, new_used_block, words[1:], original_word)
        return
        
            
        
    def findWords(self, board, words):
        self.board = board
        self.n_r = len(board)
        self.n_c = len(board[0])
        for w in words:
            for i in range(self.n_r):
                for j in range(self.n_c):
                    self.DFS(i,j, set(), w, w)
        return self.res
        

board = [["o","a","a","n"],
              ["e","t","a","e"],
              ["i","h","k","r"],
              ["i","f","l","v"]]

words = ["oath","pea","eat","rain"]

sol = Solution()
print(sol.findWords(board,words))

