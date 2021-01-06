# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        node = self
        while(node):
            print(node.val, end = "->")
            node = node.next
        print("None")

head = ListNode(0)
p = head
for i in range(1):
    node = ListNode(i,None)
    p.next = node
    p = node
    
head.print_list()

        
class Solution:
    def reverseKGroup(self, head , k):
        dummy_head = ListNode()
        p = head
        count = k
        L = []
        prev = dummy_head
        while(p):
            # add new node to list
            L.append(p)
            count -= 1
            p = p.next
            
            # reach k node reverse list and connect to prev
            if(count == 0):
                while(L):
                    prev.next = L.pop()
                    prev = prev.next
                    count = k
            print(L,":",count)
            
        if(L):
            prev.next = L[0]
        else:
            prev.next = None
        return dummy_head.next


sol = Solution()
res = sol.reverseKGroup(head,2)
res.print_list()

                
        
