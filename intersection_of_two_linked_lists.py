class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def brute_force(headA, headB):
    """
    brute force
    """
    a = headA
    b = headB
    while a:
        while b:
            if a == b:
                return a
            b = b.next
        a = a.next
        b = headB
    return None


def hash_set(headA, headB):
    nodes = set()
    node = headA
    while node:
        nodes.add(node)
        node = node.next

    node = headB
    while node:
        if node in nodes:
            return node
        node = node.next
    return None


if __name__ == '__main__':
    a = ListNode(4)
    a1 = ListNode(1)
    a.next = a1
    a2 = ListNode(8)
    a1.next = a2
    a3 = ListNode(4)
    a2.next = a3
    a4 = ListNode(5)
    a3.next = a4

    b = ListNode(5)
    b1 = ListNode(6)
    b.next = b1
    b2 = ListNode(1)
    b1.next = b2
    b2.next = a2

    # node = a
    # while node:
    #     print(node.val)
    #     node = node.next

    # print('\n\n\n')
    # node = b
    # while node:
    #     print(node.val)
    #     node = node.next

    print('intersection = ', hash_set(a, b).val)
