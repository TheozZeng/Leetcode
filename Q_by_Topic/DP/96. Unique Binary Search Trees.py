class Solution:
    def numTrees(self, n: int) -> int:
        DP = (n+1)*[0]
        #DP[num_node] = number of unique Tree with given num node
        
        # num_node = 1,2,3
        for num_node in range(n+1):

            if(num_node == 0):
                DP[0] = 1
                continue

            
            this_num = 0
            # let each node to be root [1,2,3]
            for i in range(1,num_node + 1):

                # 2 is root
                # 1 node in left tree | 1 node in right tree
                left_tree_num_node = i-1
                right_tree_num_node = num_node - i
                left_posibility = DP[left_tree_num_node]
                right_posibility = DP[right_tree_num_node]
                tot_posibility = left_posibility * right_posibility
                this_num += tot_posibility
            DP[num_node] = this_num
            #print(DP)
            
        return DP[n]


sol = Solution()
print(sol.numTrees(3))
