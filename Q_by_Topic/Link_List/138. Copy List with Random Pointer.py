
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p = head
        L = []
        Dic = {}
        
        while(p != None):
            new_p = Node(p.val)
            L.append((p,new_p))
            Dic[p] = new_p
            p = p.next
            
        for i in range(len(L)):
            t = L[i]
            old_p = t[0]
            new_p = t[1]
            
            old_next = old_p.next
            old_rand = old_p.random
            
            #print(new_p.val, ":", end="")
            
            if(old_next == None):
                new_p.next = None
                #print("next = None", end="|")
            else:
                new_next = Dic[old_next]
                new_p.next = new_next
                #print("next = ", new_next.val , end="|")
                
            if(old_rand == None):
                new_p.random = None
                #print("rand = None")
            else:
                new_rand = Dic[old_rand]
                new_p.random = new_rand
                #print("rand = ", new_rand.val )
            
        if(len(L) == 0):
            return None
        return L[0][1]
            
