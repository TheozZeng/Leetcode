class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        head = ListNode()
        dummy = head
        carry = 0
        
        while(ptr1 != None or ptr2 != None ):
            
            if(ptr1 == None):
               ptr1 = ListNode()
            if(ptr2 == None):
               ptr2 = ListNode()
               
            val = (ptr1.val + ptr2.val + carry)%10
            carry = (ptr1.val + ptr2.val + carry)//10
            
            res  = ListNode()
            res.val = val

            head.next = res
            ptr1=ptr1.next
            ptr2=ptr2.next
            head = head.next
            
        if(carry != 0):
            res  = ListNode()
            res.val = carry
            head.next = res
            
        return dummy.next

