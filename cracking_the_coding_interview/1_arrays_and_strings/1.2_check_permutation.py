def solution(s1, s2):
    chars = set()
    for char in s1:
        chars.add(char)

    for char in s2:
        if char not in chars:
            return False
    return True
