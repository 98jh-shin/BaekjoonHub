import sys
import heapq

n = int(sys.stdin.readline())

schedule = []
for _ in range(n):
    num, start, end = map(int, sys.stdin.readline().split())
    schedule.append((start, end, num))

schedule.sort()
rooms = [] # 종료시간, 강의실번호
room_count = 0
# rooms[1] = end 이들중 최소값 idx를 가져야겠지
# rooms[2] = end
res = [0] * (n + 1)
for start, end, num in schedule:
    if rooms and rooms[0][0] <= start: # 힙으로 0번째 인자가 종료시간
        prev_end, prev_num = heapq.heappop(rooms)

        res[num] = prev_num
        heapq.heappush(rooms, (end, prev_num))
    else:
        room_count += 1
        res[num] = room_count
        heapq.heappush(rooms, (end, room_count))


    # if time_min_end > start:
    #     rooms.append(end)
    #     if time_min_end > end:
    #         time_min_end = end
    #         room_idx = rooms.index(end)
    #         res[num - 1] = room_idx + 1
    # else:
    #     rooms[room_idx] = end
    #     res[num - 1] = room_idx + 1
    #     time_min_end = min(rooms)
    #     room_idx = rooms.index(time_min_end)


print(len(rooms))
for i in range(1, n + 1):
    print(res[i])