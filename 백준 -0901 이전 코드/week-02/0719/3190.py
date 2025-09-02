# import sys
#
# class queue:
#     def __init__(self):
#         self.queue = []
#     def push(self, data):
#         self.queue.append(data)
#     def pop(self):
#         if len(self.queue) <= 0:
#             return -1
#         else:
#             return self.queue.pop(0)
#
#
# dx = [1, 0, -1, 0]  # 첫 방향 오른쪽 다음 시계 방향
# dy = [0, -1, 0, 1]
#
# n = int(input())
# k = int(input())
#
# ap_list = queue()
# for i in range(k):
#     ap_list.push(map(int, sys.stdin.readline().split()))
#
# l = int(input())
#
# for i in range(l):
#     t, r = sys.stdin.readline().split()
#
# current_loc = [0, 0]
# if current_loc[0] < 0 or current_loc[1] < 0:
#     time = 0
# if current_loc[0] >= n or current_loc[1] >= n: