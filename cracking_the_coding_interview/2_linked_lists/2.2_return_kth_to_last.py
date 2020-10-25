def solution(lst, k):
    p1 = lst
    for _ in range(k):
        p1 = p1.next

    p2 = lst
    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next
    return p2
