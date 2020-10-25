class Node:
    pass


def solution(table):
    record = set()
    start = Node()
    start.next = table

    node = start
    while node.next is not None:
        if node.next.v in record:
            node.next = node.next.next
        else:
            record.add(node.next.v)
            node = node.next
    return table
