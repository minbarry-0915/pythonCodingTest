import sys
sys.stdin = open('input.txt','r')

T = 10

def calculate(base, exp):
    if exp == 0:
        return 1
    else:
        return base * calculate(base, exp - 1)

for test_case in range(10):
    case_num = int(input())
    base, exp = map(int, input().split())
    
    sum = calculate(base, exp)
    
    print(f'#{case_num} {sum}')