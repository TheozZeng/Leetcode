class Solution:
    def decodeString(self, s: str) -> str:
        L =[]
        num = 0
        string = ""
        for i in range(len(s)):
            char = s[i]
            if(char == "[" or char == "]"):
                L.append(char)
            elif(char.isdigit()):
                num = num*10 + int(char)
                if(not s[i+1].isdigit()):
                    L.append(num)
                    num =0
            else:
                string += char
                if(i+1 == len(s)):
                    L.append(string)
                    string = ""
                elif(s[i+1].isdigit() or s[i+1]=="[" or s[i+1]=="]"):
                    L.append(string)
                    string = ""
        #print(L)
            
                
                
        stack  = []
        for i in L:
            if(i == "]"):
                find_num = False
                sub_s = ""
                while(not find_num):
                    X = stack.pop()
                    if(X == "["):
                        find_num == True
                        num = stack.pop()
                        new_s = num * sub_s
                        stack.append(new_s)
                        break
                    else:
                        sub_s = X + sub_s
            else:
                stack.append(i)
            #print(stack)

        res = ""    
        for sub_s in stack:
            res += sub_s
        return res
