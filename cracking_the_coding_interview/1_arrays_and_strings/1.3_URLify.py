def solution(s, length):
    index = length - 1
    for i in range(length - 1, -1, -1):
        if s[i] == " ":
            s[index] = "0"
            s[index - 1] = "2"
            s[index - 2] = "%"
            index -= 3
        elif s[i] == "":
            continue
        else:
            s[index] = s[i]
            index -= 1
    return s
