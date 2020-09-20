from Link_list import *

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = True
        
        odd_ptr = ListNode()
        odd_l = odd_ptr
        eve_ptr = ListNode()
        eve_l = eve_ptr
        
        while(head!=None):
            if(odd):
                new_odd = ListNode()
                new_odd.val = head.val
                odd_ptr.next = new_odd
                
                odd = False
                odd_ptr = odd_ptr.next
                
            else:
                new_eve = ListNode()
                new_eve.val = head.val
                eve_ptr.next = new_eve
                
                odd = True
                eve_ptr = eve_ptr.next
            
            head = head.next

        odd_ptr.next = eve_l.next
        return odd_l.next


L = [1,2,3,4,5,6,7,8,9]
Link_list = Link_list_init(L)

sol = Solution()
New_list = sol.oddEvenList(Link_list)
Print_link_list(New_list)



        
        
