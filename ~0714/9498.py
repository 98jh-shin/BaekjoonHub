# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
"""
시험 점수를 입력받아 학점을 계산하는 프로그램. /
A program that takes exam scores as input and calculates the grade.

이 모듈은 사용자가 입력한 시험 점수를 기반으로 학점을 계산합니다.
점수가 90~100 사이일 경우 'A', 80~89 사이일 경우 'B', 70~79 사이일 경우 'C',
60~69 사이일 경우 'D', 그 외의 경우에는 'F'를 출력합니다.

Functions:
    calculate_grade(score): 점수를 기반으로 학점을 계산하여 반환합니다. /
    Calculates and returns the grade based on the score.
"""

import sys

input_score = int(sys.stdin.readline())

if 90 <= input_score <= 100:
    print('A')
elif 80 <= input_score < 90:
    print('B')
elif 70 <= input_score < 80:
    print('C')
elif 60 <= input_score < 70:
    print('D')
else:
    print('F')