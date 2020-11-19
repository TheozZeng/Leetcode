class Solution:
    def calculate(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        
        num = 0
        L = []      
        for char in s:            
            if(char.isdigit()):
                num = num*10 + int(char)
            elif(char == ' '):
                continue
            else:
                L .append(num)
                L.append(char)
                num = 0
        L .append(num)
        #print(L)

        stack = []
        i = 0
        is_postive = True
        
        while(i < len(L)):
            this = L[i]
            #print(this)
            #print(L)
            #print(stack)
            #print("-------------------------------")
            #---------------------------------------------
            if(type(this) == int):
                if(is_postive):
                    stack.append(this)
                else:
                    stack.append(-this)
            else:
                if(this == "+"):
                    is_postive = True
                elif(this == "-"):
                    is_postive = False
                elif(this == "*"):
                    num1 = stack.pop()
                    i += 1
                    num2 = L[i]
                    stack.append(num1*num2)
                else:
                    num1 = stack.pop()
                    i += 1
                    num2 = L[i]
                    #truncate toward 0
                    if(num1 > 0):
                        stack.append(num1//num2)
                    else:
                        stack.append(-(-num1)//num2)
            #---------------------------------------------
            i += 1
                        
        #print(stack)              
        return sum(stack)
 
                


s = "14/3*2"       
sol = Solution()
print(sol.calculate(s))
