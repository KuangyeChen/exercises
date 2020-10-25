def set_row_zero(mat, row):
    for i in range(len(mat[row])):
        mat[row][i] = 0


def set_col_zero(mat, col):
    for i in range(len(mat)):
        mat[i][col] = 0


def solution(mat):
    m = len(mat)
    n = len(mat[0])

    first_row_zero = False
    for i in range(n):
        if mat[0][i] == 0:
            first_row_zero = True
            break

    first_col_zero = False
    for i in range(m):
        if mat[i][0] == 0:
            first_col_zero = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    for i in range(n):
        if mat[0][i] == 0:
            set_col_zero(mat, i)
    for i in range(m):
        if mat[i][0] == 0:
            set_row_zero(mat, i)

    if first_col_zero:
        set_col_zero(mat, 0)
    if first_row_zero:
        set_row_zero(mat, 0)
    return mat
