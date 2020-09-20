# SET combine with BFS



class Solution:
    def __init__(self):
        self.found = False
        
    def BFS(self, board, word_left ,i ,j,visited):
        if(len(word_left)==0):
            self.found = True
            return
        
        elif((i,j) in visited): #this spot already visited
            return
        
        elif(self.found == True or i not in range(len(board)) or  j not in range(len(board[0]))):
            return
        
        elif(board[i][j] == word_left[0]):
            visited.add((i,j))
            self.BFS(board,word_left[1:] ,i+1,j ,visited)
            self.BFS(board,word_left[1:] ,i-1,j ,visited)
            self.BFS(board,word_left[1:] ,i ,j+1,visited)
            self.BFS(board,word_left[1:] ,i ,j-1,visited)
            visited.remove((i,j))
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                self.BFS(board,word ,i ,j ,visited)
        return self.found

