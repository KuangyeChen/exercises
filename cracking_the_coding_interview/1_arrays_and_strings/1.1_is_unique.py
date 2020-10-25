def solution_a(s):
    chars = set()
    for char in s:
        if char in chars:
            return False
        chars.add(char)
    return True


def solution_b(s):
    chars = [False for _ in range(48)]
    for char in s:
        char_int = ord(char) - ord('a')
        if chars[char_int]:
            return False
        chars[char_int] = True
    return True
