class Solution:
    def removeComments(self, source):
        res = []
        outside_comment = True
        in_block_comment = False
        in_line_comment = False
        
        for i in range(len(source)):
            this_line = source[i]
            if(not in_block_comment):
                new_line = ""

            j = 0
            while(j < len(this_line)):
                if(j <= len(this_line)-2):
                    flag = this_line[j:j+2]
                    if(flag == "/*"):
                        if(outside_comment):
                            outside_comment = False
                            in_block_comment = True
                            j+= 2
                            continue
                            
                    if(flag == "//"):
                        if(outside_comment):
                            outside_comment = False
                            in_line_comment = True
                            j += 2
                            continue
                            
 
                    if(flag == "*/"):
                        if(in_block_comment):
                            outside_comment = True
                            in_block_comment = False
                            j += 2
                            continue
                            
                if(outside_comment):
                    new_line = new_line + this_line[j]
                # increment j
                j+= 1
                    
            # finish processing a line
            if(in_line_comment):
                outside_comment = True
                in_line_comment = False
                
            if(len(new_line) >0 and not in_block_comment):
                res.append(new_line)

        return res                
                       
                        
                    
                

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
sol = Solution()
sol.removeComments(source)
        
