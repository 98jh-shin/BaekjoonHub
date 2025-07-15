n = int(input())

count = 0

used_col = [False] * n
queen_pos_left = [False] * (2 * n) # 우하단으로 갈때 row - col 이 일정 음수 가능성 있어서 (n - 1) + (row - col)
queen_pos_right = [False] * (2 * n) # 좌한으로 갈때 row + col 이 일정

def chess(row):

    global count

    if row == n:
        count += 1
        return

    for col in range(n):
        if not used_col[col] and not queen_pos_right[(n - 1) + (row - col)] and not queen_pos_left[row + col]:
            used_col[col] = True
            queen_pos_left[row + col] = True
            queen_pos_right[(n - 1) + (row - col)] = True

            chess(row + 1)

            used_col[col] = False
            queen_pos_left[row + col] = False
            queen_pos_right[(n - 1) + (row - col)] = False

chess(0)


print(count)


