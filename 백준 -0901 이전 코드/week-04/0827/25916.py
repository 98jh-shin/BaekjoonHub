import sys

def solve():
    """
    백준 25916번 "싫은데요" 문제 해결
    투 포인터(Two Pointers) 알고리즘을 사용한 연속 부분 구간 최대값 찾기
    """
    # ========== 입력 처리 ==========
    N, M = map(int, sys.stdin.readline().split())
    # N: 구멍의 개수
    # M: 햄스터가 막을 수 있는 최대 부피

    holes = list(map(int, sys.stdin.readline().split()))
    # holes[i]: i번째 구멍의 부피

    # ========== 투 포인터 초기화 ==========
    left = 0        # 왼쪽 포인터 (구간의 시작)
    right = 0       # 오른쪽 포인터 (구간의 끝)
    current_sum = 0 # 현재 구간의 부피 합
    max_volume = 0  # 지금까지 찾은 최대 부피

    # ========== 투 포인터 알고리즘 실행 ==========
    while right < N:
        # ========== Step 1: 오른쪽 포인터 확장 ==========
        # 현재 구간에 right번째 구멍 추가
        current_sum += holes[right]

        # ========== Step 2: 부피 초과 시 왼쪽 포인터 이동 ==========
        # 현재 구간의 부피가 M을 초과하면 왼쪽에서 구멍들을 제거
        while current_sum > M and left <= right:
            current_sum -= holes[left]
            left += 1

        # ========== Step 3: 최대값 업데이트 ==========
        # 현재 구간이 조건을 만족하면 (current_sum <= M) 최대값 갱신
        if current_sum <= M:
            max_volume = max(max_volume, current_sum)

        # ========== Step 4: 오른쪽 포인터 이동 ==========
        right += 1

    return max_volume

# ========== 메인 실행 ==========
print(solve())


"""
========== 알고리즘 상세 분석 ==========

1. 핵심 아이디어: 투 포인터 (Two Pointers)
   - 연속된 부분 구간에서 조건을 만족하는 최대값 찾기
   - left, right 두 포인터로 구간을 동적으로 조절

2. 알고리즘 동작 과정:
   (1) right 포인터를 오른쪽으로 이동하며 구간 확장
   (2) 부피 합이 M을 초과하면 left 포인터를 이동하여 구간 축소
   (3) 조건을 만족하는 구간에서 최대값 업데이트
   (4) right가 배열 끝에 도달할 때까지 반복

3. 시간 복잡도: O(N)
   - left와 right 포인터가 각각 최대 N번 이동
   - 전체적으로 배열을 한 번 순회

4. 공간 복잡도: O(1)
   - 입력 배열을 제외하고 상수 공간만 사용

========== 예시 실행 과정 ==========
입력: N=8, M=9
holes = [1, 2, 3, 1, 2, 4, 3, 2]

초기 상태: left=0, right=0, current_sum=0, max_volume=0

Step 1: right=0, current_sum=1, max_volume=1
Step 2: right=1, current_sum=3, max_volume=3
Step 3: right=2, current_sum=6, max_volume=6
Step 4: right=3, current_sum=7, max_volume=7
Step 5: right=4, current_sum=9, max_volume=9
Step 6: right=5, current_sum=13 > 9
        left=0→1, current_sum=12
        left=1→2, current_sum=10  
        left=2→3, current_sum=7, max_volume=9
...

최종 답: 9 (6번째부터 8번째 구멍: 4+3+2=9)

========== 핵심 포인트 ==========
1. 연속된 부분 구간 문제 → 투 포인터 적합
2. 부피 합이 조건 초과 시 왼쪽 포인터로 구간 축소
3. 매 단계마다 조건 만족 시 최대값 갱신
4. 포인터가 역행하지 않아 효율적인 O(N) 해결

========== 주의사항 ==========
1. left <= right 조건 확인 (포인터 교차 방지)
2. 빈 구간(current_sum=0) 처리
3. 최대값 갱신 시점 정확히 파악
"""