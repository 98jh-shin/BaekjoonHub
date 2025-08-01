n = int(input())

count = 0
used_col = [False] * n
left_pos = [False] * (2 * n)
right_pos = [False] * (2 * n)


def chess(row):
    global count

    if row == n:
        count += 1
        return

    for col in range(n):
        if used_col[col] or left_pos[col + row] or right_pos[(n - 1) + (row - col)]:
            continue

        used_col[col] = True
        left_pos[row + col] = True
        right_pos[(n - 1) + (row - col)] = True

        chess(row + 1)

        used_col[col] = False
        left_pos[row + col] = False
        right_pos[(n - 1) + (row - col)] = False


chess(0)
print(count)
