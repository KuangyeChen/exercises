def solution(s):
    count = dict()
    for char in s:
        count = count.get(char, 0) + 1

    odd = len(s) % 2 == 1
    count_1 = 0
    for k, v in count:
        if v % 2 == 1 and not odd:
            return False
        elif v % 2 == 1 and odd:
            if count_1 == 1:
                return False
            count_1 = 1
    return True
