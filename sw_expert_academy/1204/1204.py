import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def update_count(grade_count, grade):
    if grade not in grade_count:
        grade_count[grade] = 1
    else:
        grade_count[grade] += 1
    
    
for test_case in range(1, T+1):
    case_num = int(input())
    grades = list(map(int, input().split()))
    grades_count = {}
    for grade in grades:
        update_count(grades_count, grade)

    max_grade = max(grades_count, key=grades_count.get)
    print(f'#{test_case} {max_grade}')