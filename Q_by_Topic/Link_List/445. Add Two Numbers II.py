from Link_List import *

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        L1 = []
        L2 = []
        p1 = l1
        p2 = l2
        while(p1):
            L1.append(p1.val)
            p1=p1.next
        while(p2):
            L2.append(p2.val)
            p2=p2.next
        print(L1)
        print(L2)

        max_len = max(len(L1),len(L2))
        carry = 0
        prev_node = None
        this_node = None
        
        while(max_len > 0):
            n1 = 0
            n2 = 0
            if(L1):
                n1 = L1.pop()
            if(L2):
                n2 = L2.pop()
            this_n = (n1 + n2 + carry)%10
            carry = (n1 + n2 + carry)//10
            print(max_len,":", n1,"-",n2,"|",this_n,"-",carry)
            this_node = ListNode(this_n,prev_node)
            prev_node = this_node
            max_len -= 1

        if(carry > 0):
            this_node = ListNode(carry,prev_node)
        return this_node
            

l1 = init_link_list([1,2,3,4,5,6,7,8,9])
l2 =  init_link_list([9,9,9,9,9,9,9,9,9])
sol = Solution()
res = sol.addTwoNumbers(l1,l2)
print_link_list(res)
    
