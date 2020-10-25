def solution(l1, l2):
    node = l1
    len_1 = 0
    while node is not None:
        len_1 += 1
        node = node.next

    node = l2
    len_2 = 0
    while node is not None:
        len_2 += 1
        node = node.next

    node_1 = l1
    node_2 = l2
    if len_1 < len_2:
        for _ in range(len_2 - len_1):
            node_2 = node_2.next
    else:
        for _ in range(len_1 - len_2):
            node_1 = node_1.next

    while node_1 is not None:
        if node_1 is node_2:
            return node_1
        node_1 = node_1.next
        node_2 = node_2.next
    return None
