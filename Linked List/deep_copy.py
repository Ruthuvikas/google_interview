"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        ptr = head
        #add old and new node side by side
        while ptr:
            new_node = Node(ptr.val)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        ptr = head
        #link copy node random 
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        #Unweave the LL
        ptr_old_list = head
        ptr_new_list = head.next
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = (
                ptr_new_list.next.next if ptr_new_list.next else None
            )
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new

#T : O(n)
#S: O(1)
