# CMake 최소 요구 버전 설정
cmake_minimum_required(VERSION 3.10)

# 프로젝트 이름과 사용할 언어(C++) 설정
project(BaekjunHub CXX)

# C++ 표준을 17로 설정 (원하면 14나 20으로 변경 가능)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ------------------------------------------------------------------
# 여기에 C++로 풀 문제들을 하나씩 실행 파일(target)로 추가합니다.
# 사용법: add_executable(타겟이름 소스파일_경로)
# '타겟이름'은 CLion의 실행 목록에 표시될 이름입니다.
# ------------------------------------------------------------------

# 예시: 1874번 스택 수열 문제를 'BaekjunHub/1874_Stack_Sequence/main.cpp' 경로에 만들었다면
add_executable(cppScratchpad cppScratchpad/main.cpp)

# 예시: 1000번 A+B 문제를 'BaekjunHub/1000_A_plus_B/main.cpp' 경로에 만들었다면
# add_executable(1000_A_plus_B 1000_A_plus_B/main.cpp)