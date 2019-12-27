class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ll = ListNode(-1)
        header = ll
        while l1 and l2:
            if l1.val <= l2.val:
                ll.next = l1
                l1 = l1.next
            else:
                ll.next = l2
                l2 = l2.next
            ll = ll.next
        if l1 is None:
            ll.next = l2
        else:
            ll.next = l1
        return header.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

x = ListNode(1)
y = ListNode(3)
z = ListNode(4)
x.next = y
y.next = z

res = Solution().mergeTwoLists(a, x)
print(res)
