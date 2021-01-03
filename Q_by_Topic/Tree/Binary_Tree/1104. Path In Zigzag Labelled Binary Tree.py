class Solution:
    def pathInZigZagTree(self, label):
        L = [None] * (label + 1)
        
        level = 0
        num_base = 0
        
        prev_row = [None]
        this_row= []
        for i in range(1,label+1):
            nums_in_level = 2**level
            if(i <= num_base + nums_in_level):
                this_row.append(i)
                # find parent val of this node
                parent_index  = (len(this_row)-1)//2
                parent_val = prev_row[len(prev_row)-1-parent_index]
                L[i] = parent_val
                print(L[:i+1])
                
            if(i == num_base + nums_in_level):
                print(this_row)
                prev_row = this_row
                this_row = []
                
                level += 1
                num_base += nums_in_level

        res = []
        while(label != None):
            res.append(label)
            label = L[label]
        return res[::-1]

 
 

                
sol = Solution()
print(sol.pathInZigZagTree(26))
