from collections import deque 

class Solution:
    def jump(self, nums):
        #basic dikstra idea
        reached = deque([(0,0)])
        visited_set = set()
        reached_set = set()
        while(reached):
            print(reached)
            print(visited_set)
            this_node = reached.popleft()
            this_index = this_node[1]
            this_cost = this_node[0]
            visited_set.add(this_index)
            # visit from target node
            if(this_index == len(nums)-1):
                return this_cost
            #add adj node to reached
            this_len = nums[this_index]
            for i in range(1,this_len+1):
                next_index = this_index + i
                if(next_index not in reached_set and next_index not in reached_set and next_index < len(nums)):
                    reached.append((this_cost+1,next_index))
                    reached_set.add(next_index)
        
                    
                    
        
        
        
        

nums = [5,8,1,8,9,8,7,1,7]
sol = Solution()
print(sol.jump(nums))
