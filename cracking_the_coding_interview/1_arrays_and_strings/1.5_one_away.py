def solution(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    s_long = s1 if len(s1) > s2 else s2
    s_short = s1 if len(s1) < s2 else s2
    i, j = 0, 0
    one_edit = False
    while i < len(s_long) and j < len(s_short):
        if s_long[i] != s_short[j]:
            if one_edit:
                return False
            one_edit = True
            if len(s_long) == len(s_short):
                j += 1
        else:
            j += 1
        i += 1
    return True
