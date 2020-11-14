class Solution:
    def merge_2_list(self,L,R):
        i = j = k = 0
        arr = [None]*(len(L)+len(R))
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr

    def merge_sort_matrix(self,matrix):
        if(len(matrix)== 0):
            return []
        elif(len(matrix)==1):
            return matrix[0]
        elif(len(matrix)==2):
            return self.merge_2_list(matrix[0],matrix[1])
        
        else:
            mid_row = len(matrix)//2
            up_matrix = matrix[:mid_row]
            low_matrix = matrix[mid_row:]
            up_list = self.merge_sort_matrix(up_matrix)
            low_list = self.merge_sort_matrix(low_matrix)
            return self.merge_2_list(up_list,low_list)

    def kthSmallest(self, matrix, k):
        L = self.merge_sort_matrix(matrix)
        print(L)
        return L[k-1]

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
sol = Solution()
print(sol.kthSmallest(matrix, k))
