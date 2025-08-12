import sys

# N: 멀티탭 구멍의 개수, K: 전기용품의 총 사용횟수
N, K = map(int, sys.stdin.readline().split())

# 전기용품 사용 순서
schedule = list(map(int, sys.stdin.readline().split()))

plug = set() # 현재 멀티탭에 꽂혀있는 제품 리스트
unplug_count = 0  # 플러그를 뽑은 횟수

# 사용 순서대로 순회
for i, item in enumerate(schedule):
    if item in p  continue

    if len(plug) < N:
        plug.append(item)
        continue

    item_to_unplug = -1
    lastest_use_idx = -1

    for pluged_item in plug:
        next_use = K
        for j in range(i + 1, K):
            if schedule[j] == pluged_item:
                next_use = j
                break
        if next_use > lastest_use_idx:
            lastest_use_idx = next_use
            item_to_unplug = pluged_item

    plug.remove(item_to_unplug)
    unplug_count += 1
    plug.append(item)

print(unplug_count)