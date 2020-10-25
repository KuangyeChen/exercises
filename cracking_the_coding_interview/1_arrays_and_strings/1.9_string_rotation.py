def is_substring(s1, s2):
    pass


def solution(s1, s2):
    if len(s1) != len(s2):
        return False
    return is_substring(s1, s2 + s2)
