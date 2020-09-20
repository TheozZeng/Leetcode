class Solution:
    def myAtoi(self, str: str) -> int:
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', " ", "+", "0"]
        store = ""
        for index, char in enumerate(str):
            #begin with non num or " "
            if index == 0 and char not in number:
                return 0
            #end find last num
            elif char not in number:
                return self.compute_ans(store)
            
            if char in number:
                #skip " "                
                if char == " " and store == "":
                    continue
                #number end in " "
                elif char == " " and store != "":
                    return self.compute_ans(store)
                elif char in ["-", "+"] and store != "":
                    return self.compute_ans(store)
                store += char
        return self.compute_ans(store)
      
    def compute_ans(self, value):

        try:
            if int(value) >= 2**31:
                return 2**31 - 1
            elif int(value) <= (-2)**31:
                return (-2)**31 
            return int(value)
        except ValueError:
            return 0


str = "   -1234 90My"
sol = Solution()
print(sol.myAtoi(str))