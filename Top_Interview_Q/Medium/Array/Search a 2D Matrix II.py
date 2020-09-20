class Solution:
	def search_helper(self,r1,c1,r2,c2,matrix,target):
		rm = (r1+r2)//2
		cm = (c1+c2)//2
		m_val = matrix[rm][cm]
		print(r1,c1,r2,c2,"|",m_val)
		if(r1>r2 or c1>c2):
			return False

		if(r1==r2 and c1==c2):
			if(m_val != target):
				return False

		if(m_val == target):
			return True

		elif(m_val > target):
			if self.search_helper(r1,c1,rm-1,cm-1,matrix,target):
				return True
			elif self.search_helper(r1,cm,rm-1,c2,matrix,target):
				return True
			elif self.search_helper(rm,c1,r2,cm-1,matrix,target):
				return True
			else:
				return False

		else:
			if self.search_helper(rm+1,cm+1,r2,c2,matrix,target):
				return True 
			elif self.search_helper(r1,cm+1,rm,c2,matrix,target):
				return True 
			elif self.search_helper(rm+1,c1,r2,cm,matrix,target):
				return True
			else:
				return False


	def searchMatrix(self, matrix, target):
		n_r = len(matrix)
		if(n_r == 0):
			return False
		else:
			n_c = len(matrix[0])
			if(n_c == 0):
				return False

		return self.search_helper(0,0,n_r-1,n_c-1,matrix,target)






matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

sol = Solution()
print(sol.searchMatrix(matrix,20))
        