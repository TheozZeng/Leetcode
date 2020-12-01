class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if(numerator%denominator == 0):
            return str(numerator//denominator)

        # XXX
        sign = ""
        if(numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        main_part = sign + str(numerator // denominator)

        #_____. YYY
        remain_part = ""
        remainder = numerator % denominator     
        remainder *= 10
        S = {}
        while(remainder):
            if(remainder in S):
                break
            a= remainder // denominator
            b = remainder % denominator
            S[remainder] = (a,b)
            remain_part += str(a)
            #print(remainder,":",S[remainder])
            remainder = b*10
        
        if(remainder == 0):
            return main_part+"."+remain_part
        else:
            #print("---track recurring---")
            T = S[remainder]
            a = T[0]
            b = T[1]
            loop = str(a)
            while(b*10 != remainder):
                b *= 10
                T = S[b]
                a = T[0]
                b = T[1]
                loop += str(a)
                print(loop)

            i = remain_part.index(loop)
            return main_part+"."+remain_part[:i]+"("+loop+")"

numerator = 1
denominator = 132
sol = Solution()
print(sol.fractionToDecimal(numerator, denominator))
