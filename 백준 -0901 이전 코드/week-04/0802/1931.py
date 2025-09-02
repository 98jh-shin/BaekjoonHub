import sys
import queue
N = int(sys.stdin.readline())

def add_conf():
    conf = []
    for i in range(N):
        s, e = map(int, sys.stdin.readline().split())  # 시작시간 종료시간
        conf.append((s, e)) # 시작시간 정렬
    conf.sort()
    return conf

def greedy(conf):
    time = sys.maxsize
    count = 0
    while conf:
        s, e = conf.pop() # 거꾸로 풀어보자 시작시간 종료시간 시작시간이 제일 늦은거부터
        if time < e:
            continue
        count += 1
        time = s
    return count

print(greedy(add_conf()))