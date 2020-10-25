def solution(m):
    n = len(m)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    # Flip
    for i in range(n):
        for j in range(n // 2 + 1):
            m[i][j], m[i][n - j - 1] = m[i][n - j - 1], m[i][j]
    return m
