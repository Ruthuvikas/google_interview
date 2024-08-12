# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next
        while list1:
            tail.next = ListNode(list1.val)
            list1 = list1.next
            tail = tail.next
        while list2:
            tail.next = ListNode(list2.val)
            list2 = list2.next
            tail = tail.next
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergeLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergeLists.append(self.merge(l1, l2))
            lists = mergeLists
        return lists[0] if lists[0] else None

#T: O(nlogk)
#S: O(1)