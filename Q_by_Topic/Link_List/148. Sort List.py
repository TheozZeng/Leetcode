# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def break_link_list(self, head):
        p = head
        length = 0
        while(p != None):
            print(p.val)
            length += 1
            p = p.next
            
        mid = length//2
        
        p = head
        n = 0
        while(n < mid-1):
            p = p.next
            n += 1
        p1 = head
        p2 = p.next
        p.next = None
        #print("---",p1.val,"|",p2.val,"---")
        return[p1,p2]
        
    
    def mergelist(self, p1,p2):
        
        dummy = ListNode()
        p = dummy
        while(p1 != None and p2!= None):
            if(p1.val < p2.val):
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
                   
            p = p.next
            
        if(p1 == None):
            p.next = p2
        else:
            p.next = p1
        return dummy.next
        
        
    def sortList(self, head: ListNode) -> ListNode:
        if(head == None):
            return None
        elif(head.next == None):
            return head
        
        l = self.break_link_list(head)
        l1 = l[0]
        l2 = l[1]
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        
        res = self.mergelist(l1,l2)
        return res
        
