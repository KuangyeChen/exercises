class Node:
    def __init__(self, v):
        pass


def solution(lst):
    rev_node = Node(lst.v)
    node = lst.next
    while node is not None:
        next_node = Node(node.v)
        next_node.next = rev_node
        rev_node = next_node

    node = lst
    while node is not None:
        if node.v != rev_node.v:
            return False
        node = node.next
        rev_node = rev_node.next
    return True
