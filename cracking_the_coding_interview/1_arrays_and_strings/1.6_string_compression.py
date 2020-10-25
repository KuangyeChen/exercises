def solution(s):
    res = ""
    index = 0
    while index < len(s):
        i = index
        while i < len(s) and s[index] == s[i]:
            i += 1
        res += "{}{}".format(i - index, s[index])
        index = i

    return s if len(res) >= s else res
