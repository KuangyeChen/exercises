def solution(lst):
    walker = lst
    runner = lst
    while runner is not None and runner.next is not None:
        walker = walker.next
        runner = runner.next.next
        if walker is runner:
            break

    if walker is not runner:
        return None

    p = lst
    while p is not runner:
        p = p.next
        runner = runner.next
    return p
