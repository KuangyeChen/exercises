def solution(node):
    while node.next is not None:
        node.v = node.next.v
        if node.next.next is None:
            node.next = None
    return
