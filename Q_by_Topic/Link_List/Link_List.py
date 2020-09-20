# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def init_link_list(L):
    head = ListNode()
    ptr = head
    
    for i in L:
        node = ListNode()
        node.val = i
        ptr.next = node
        ptr = ptr.next

    return head.next

def print_link_list(node):
    ptr = node
    while(ptr != None):
        print(ptr.val, end="->")
    print("None")

L = [0,1,2,3,4,5,6,7,8]
head = init_link_list(L)
print_link_list(head)
