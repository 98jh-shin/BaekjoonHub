import sys

def solve():
    """
    회전 초밥 문제 해결
    슬라이딩 윈도우 + 해시맵을 이용한 효율적 풀이
    """
    # ========== 입력 처리 ==========
    N, d, k, c = map(int, sys.stdin.readline().split())
    # N: 초밥 벨트에 놓인 접시 수
    # d: 초밥의 가짓수 (1번부터 d번까지)
    # k: 연속해서 먹는 접시 수
    # c: 쿠폰으로 무료로 먹을 수 있는 초밥 번호
    
    # 초밥 벨트 정보 (원형 구조)
    sushi = []
    for _ in range(N):
        sushi.append(int(sys.stdin.readline().strip()))
    
    # ========== 슬라이딩 윈도우 초기화 ==========
    # 각 초밥 종류별 개수를 세는 딕셔너리
    sushi_count = {}
    
    # 첫 번째 윈도우 (0번부터 k-1번까지) 설정
    for i in range(k):
        if sushi[i] in sushi_count:
            sushi_count[sushi[i]] += 1
        else:
            sushi_count[sushi[i]] = 1
    
    # 쿠폰 초밥은 항상 먹을 수 있으므로 추가
    # if c in sushi_count:
    #     sushi_count[c] += 1
    # else:
    #     sushi_count[c] = 1
    
    # 현재 윈도우에서 먹을 수 있는 초밥 종류 개수
    max_variety = len(sushi_count)
    
    # ========== 슬라이딩 윈도우로 전체 탐색 ==========
    # 원형 구조이므로 N번 이동하면 원래 자리로 돌아옴
    for i in range(N):
        # ========== 윈도우 이동: 왼쪽 끝 제거 ==========
        # 현재 윈도우의 맨 앞 초밥 제거
        left_sushi = sushi[i]
        sushi_count[left_sushi] -= 1
        
        # 개수가 0이 되면 딕셔너리에서 완전 제거
        if sushi_count[left_sushi] == 0:
            del sushi_count[left_sushi]
        
        # ========== 윈도우 이동: 오른쪽 끝 추가 ==========
        # 새로운 윈도우의 맨 뒤 초밥 추가
        # 원형 구조 처리: (i + k) % N
        right_sushi = sushi[(i + k) % N]
        
        if right_sushi in sushi_count:
            sushi_count[right_sushi] += 1
        else:
            sushi_count[right_sushi] = 1
        
        # ========== 쿠폰 초밥 처리 ==========
        # 쿠폰 초밥은 항상 무료로 먹을 수 있음
        # if c not in sushi_count:
        #     sushi_count[c] = 1
        
        # ========== 최대값 업데이트 ==========
        # 현재 윈도우에서 먹을 수 있는 초밥 종류 개수
        current_variety = len(sushi_count)
        if c not in sushi_count:
            current_variety += 1
        max_variety = max(max_variety, current_variety)
    
    return max_variety

# ========== 메인 실행 ==========
print(solve())


"""
========== 알고리즘 상세 분석 ==========

1. 핵심 아이디어: 슬라이딩 윈도우 (Sliding Window)
   - 크기 k인 윈도우를 한 칸씩 이동하면서 최적해 탐색
   - 매번 전체를 다시 계산하지 않고, 변화분만 업데이트

2. 원형 구조 처리:
   - 인덱스 (i + k) % N을 사용하여 배열 끝에서 처음으로 순환
   - 마지막 접시 다음은 첫 번째 접시

3. 쿠폰 초밥 처리:
   - 매 윈도우마다 쿠폰 초밥이 포함되어 있는지 확인
   - 없으면 무료로 추가 가능하므로 종류 개수에 포함

4. 시간 복잡도: O(N)
   - 각 윈도우마다 O(1) 연산 (해시맵 사용)
   - 전체 N개의 윈도우 처리

5. 공간 복잡도: O(d)
   - 최대 d개의 서로 다른 초밥 종류 저장

========== 예시 실행 과정 ==========
입력: N=8, d=30, k=4, c=30
초밥: [7, 9, 7, 30, 2, 7, 9, 25]

초기 윈도우 [7,9,7,30]: {7:2, 9:1, 30:2} →
"""