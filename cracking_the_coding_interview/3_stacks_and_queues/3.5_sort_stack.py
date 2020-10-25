def solution(s):
    s2 = [s.pop()]
    while len(s) > 0:
        tmp = s.pop()
        if s2[-1] >= tmp:
            s2.append(tmp)
            continue

        while len(s2) > 0 and s2[-1] < tmp:
            s.append(s2.pop())
        s2.append(tmp)
    return s2
