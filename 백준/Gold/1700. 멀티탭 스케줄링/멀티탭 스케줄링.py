import sys

N, K = map(int, sys.stdin.readline().split())

schedule = list(map(int, sys.stdin.readline().split()))

plug = set()
unplug_count = 0

for i in range(K):
    item = schedule[i]
    if item in plug:
        continue
    
    if len(plug) < N:
        plug.add(item)
        continue
    
    last_idx = -1
    item_to_unplug = -1
    
    for pluged_item in plug:
        next_use = K
        for j in range(i + 1, K):
            if schedule[j] == pluged_item:
                next_use = j
                break
        
        if next_use > last_idx:
            last_idx = next_use
            item_to_unplug = pluged_item
    
    unplug_count += 1
    plug.remove(item_to_unplug)
    plug.add(item)

print(unplug_count)