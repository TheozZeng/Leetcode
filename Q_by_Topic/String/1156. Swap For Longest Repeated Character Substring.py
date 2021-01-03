class Solution:
    def maxRepOpt1(self, text):
        D = {}
        prev = None
        prev_i = 0
        text += "|"
        for i in range(len(text)):
            c = text[i]
            print(i,":",c)
            if(prev == None or prev != c):
                if(prev not in D):
                    D[prev] = [[prev_i,i]]
                else:
                    D[prev].append([prev_i,i])
                prev = c
                prev_i = i
                
        D.pop(None, None)
        print(D)

        res = 0
        # try to connect 2 adj lists
        for char, L in D.items():
            print(char,L)
            for i in range(len(L)):
                #connect to next list
                if(i < len(L)-1):
                    l1 = L[i]
                    l2 = L[i+1]
                    # can connect
                    if(l1[1]+1 == l2[0]):
                        if(len(L) >= 3):
                            new_res = (l1[1] - l1[0]) + (l2[1] - l2[0]) + 1
                        else:
                            new_res = (l1[1] - l1[0]) + (l2[1] - l2[0])
                        res = max(res,new_res)
                #cannot connect just extend
                l = L[i]
                if(len(L) >= 2):
                    new_res = (l[1] - l[0]) + 1
                else:
                    new_res = (l[1] - l[0])
                res = max(res,new_res)
                print(L[i], res)   
                
        return res



text = "aaabbaaa"
sol = Solution()
print(sol.maxRepOpt1(text))
