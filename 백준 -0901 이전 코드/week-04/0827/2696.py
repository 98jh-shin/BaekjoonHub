import sys
import heapq

def solve():
    M = int(input())

    # 입력이 여러 줄에 걸쳐 올 수 있음
    numbers = []
    while len(numbers) < M:
        line = list(map(int, input().split()))
        numbers.extend(line)

    numbers = numbers[:M]

    max_heap = []  # 작은 절반을 담는 최대 힙 (음수로 저장)
    min_heap = []  # 큰 절반을 담는 최소 힙

    medians = []

    for i in range(M):
        num = numbers[i]

        # 첫 번째 원소는 max_heap에 추가
        if not max_heap:
            heapq.heappush(max_heap, -num)
        else:
            # max_heap의 최댓값(루트)과 비교
            if num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        elif len(min_heap) > len(max_heap):
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)

        # 홀수번째(1-based)일 때 중앙값 저장
        if (i + 1) % 2 == 1:
            medians.append(-max_heap[0])

    # 출력 형식에 맞게 출력
    print(len(medians))
    for i in range(0, len(medians), 10):
        print(' '.join(map(str, medians[i:i+10])))

T = int(input())
for _ in range(T):
    solve()