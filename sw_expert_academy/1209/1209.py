
import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    case_number = int(input())
    #2차원 행렬 생성
    #한줄에 100개의 숫자 100개의 줄이므로
    matrix = [list(map(int, input().split())) for _ in range(100)]

    row_sum = []
    for row in matrix:
        row_sum.append(sum(row))

    col_sum = []
    for col in range(100):
        total = 0
        for row in range(100):
            total += matrix[row][col]
        col_sum.append(total)

    diagonal_sum_1 = sum(matrix[i][i] for i in range(100))
    diagonal_sum_2 = sum(matrix[i][99-i] for i in range(100))

    max_sum = max(max(row_sum), max(col_sum), diagonal_sum_1, diagonal_sum_2)

    print(f'{test_case} {max_sum}')
    # ///////////////////////////////////////////////////////////////////////////////////
