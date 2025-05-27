# 입력 받기
A = int(input())
B = int(input())

# B의 각 자리 숫자 분리
B_ones = B % 10          # 1의 자리
B_tens = (B // 10) % 10  # 10의 자리
B_hundreds = B // 100    # 100의 자리

# 곱셈 과정 출력
print(A * B_ones)         # (3) 위치 값
print(A * B_tens)         # (4) 위치 값
print(A * B_hundreds)     # (5) 위치 값
print(A * B)              # (6) 위치 값 (최종 결과)
