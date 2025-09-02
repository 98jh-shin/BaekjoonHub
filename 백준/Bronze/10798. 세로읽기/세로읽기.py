import sys

result = [list(sys.stdin.readline().rstrip()) for _ in range(5)]

max_len = max(len(row) for row in result)

print("".join(result[row][col] for col in range(max_len) for row in range(5) if col < len(result[row])))