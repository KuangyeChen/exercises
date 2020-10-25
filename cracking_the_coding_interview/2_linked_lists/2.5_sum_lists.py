class Node:
    pass


def solution(l1, l2):
    res = 0
    l3 = Node()
    while l1 is not None or l2 is not None:
        l3.next = Node()
        l3.next.v = 0
        if l1 is not None:
            l3.next.v += l1.v
        if l2 is not None:
            l3.next.v += l2.v
        l3.next.v += res
        res = l3.next.v // 10
        l3.next.v %= 10
    return l3
