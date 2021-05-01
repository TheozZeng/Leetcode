class Solution:
    def __init__(self):
        self.s = ""
        
    def find_sub_string(self, char_count, start, end):
        
        if(char_count[0] and char_count[1] and char_count[2]):
            return [char_count, end]
            
        for j in range(end+1,len(self.s)):
            char = self.s[j]
            if(char == "a"):
                char_count[0] += 1
            if(char == "b"):
                char_count[1] += 1
            if(char == "c"):
                char_count[2] += 1
            if(char_count[0] and char_count[1] and char_count[2]):
                return [char_count, j]
            
        return [char_count, len(self.s)]
    
        
    def numberOfSubstrings(self, s: str) -> int:
        self.s = s
        res = 0

        char_count = None
        for i in range(len(s)):
            if(i==0):
                find_sub_string_res = self.find_sub_string([0,0,0],0,-1)
            else:
                prev_c = s[i-1]
                prev_char_count = char_count
                if(prev_c == "a"):
                    prev_char_count[0] -= 1
                if(prev_c == "b"):
                    prev_char_count[1] -= 1
                if(prev_c == "c"):
                    prev_char_count[2] -= 1
                find_sub_string_res = self.find_sub_string(prev_char_count,i,end_index)
                
            char_count = find_sub_string_res[0]
            end_index = find_sub_string_res[1]
            res += (len(s) - end_index)
                
        return res


s = "abcabc"
sol = Solution()
print(sol.numberOfSubstrings(s))
        
