class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ph = ListNode(-1)
        prev = ph
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1:
            prev.next = l1
        else:
            prev.next = l2
        return ph.next


if __name__ == '__main__':
    a = ListNode(1)
    a1 = ListNode(3)
    a.next = a1
    a2 = ListNode(5)
    a1.next = a2

    b = ListNode(1)
    b1 = ListNode(2)
    b.next = b1
    b2 = ListNode(6)
    b1.next = b2

    node = a
    while node:
        print(node.val)
        node = node.next
    print('\n')
    node = b
    while node:
        print(node.val)
        node = node.next


    solution = Solution()
    head = solution.mergeTwoLists(a, b)
    print('\n')
    node = head
    while node:
        print(node.val)
        node = node.next
