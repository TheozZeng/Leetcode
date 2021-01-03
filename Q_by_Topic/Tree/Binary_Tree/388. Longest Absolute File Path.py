class Solution:
    def lengthLongestPath(self, input: str) -> int:
        #print(input)
        lines = input.split("\n")
        #print(lines)
        
        level = []
        max_len = 0
        
        for line in lines:
            n_level = line.count('\t')
            cur = line.strip('\t')
            cur_len = len(cur)
            
            is_file = False
            # file found
            if("." in cur):
                is_file = True
            if(n_level !=0):
                cur_len += 1 
                
            if(n_level == len(level)):
                level += [cur_len]
            else:
                level[n_level] = cur_len
                
            if(is_file):
                len_path = sum(level[:n_level + 1])
                max_len = max(max_len,len_path)
        return max_len
                
            
