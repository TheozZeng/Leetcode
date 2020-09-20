class Solution:
    def __init__(self):
        self.found = False
        
    def BFS(self,board,word_left ,i ,j):
        print("__________________________________________")
        board[i][j] = "$"
        print_board(board)
        '''
        if(self.found == True or i not in range(len(board)) or  j not in range(len(board[0]))):
            return
        if(len(word_left)==0):
            self.found = True
            return
        
        if(board[i][j] == word_left[0]):
            
            print("__________________________________________")
            print(word_left)
            print_board(board)
            
            temp_board = []
            temp_board[:] = board
            temp_board[i][j] = "*"
            
            self.BFS(temp_board,word_left[1:] ,i+1,j)
            self.BFS(temp_board,word_left[1:] ,i-1,j)
            self.BFS(temp_board,word_left[1:] ,i ,j+1)
            self.BFS(temp_board,word_left[1:] ,i ,j-1)
        '''
        
        
    def exist(self, board, word) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.BFS(board.copy(),word,i ,j)
        return self.found

#---------------------------------------------------------------------------------
def print_board(board):
    for r in board:
        for c in r:
            print(c,end="|")
        print("")

#---------------------------------------------------------------------------------
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "SEE"

sol = Solution()
print(sol.exist(board,word))
