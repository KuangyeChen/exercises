class Node:
    pass


def solution(l1, x):
    before = Node()
    after = Node()
    after_head = after

    node = l1
    while node is not None:
        if node.v < x:
            before.next = node
            before = before.next
        else:
            after.next = node
            after = after.next
    before.next = after_head.next
