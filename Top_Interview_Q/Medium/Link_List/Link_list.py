#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Link_list_init(L):
    ptr= ListNode()
    dummy_head = ptr
    
    for i in L:
        new_node = ListNode(i,None)
        ptr.next = new_node
        ptr = ptr.next
    return dummy_head.next

def Print_link_list(head):
    ptr = head
    while(ptr!=None):
        print(ptr.val,"->",end="")
        ptr=ptr.next
    print("None")

'''
L = [1,2,3,4,5,6,7]
Link_list = Link_list_init(L)
Print_link_list(Link_list)
'''
        
