import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

code_patterns = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

def decode_line(line):
    end = line.rfind('1')
    if end == -1:
        return []
    start = end - 55
    code_str = line[start: end + 1]

    digits = []
    for i in range(0,56,7):
        segment = code_str[i: i + 7]
        if segment in code_patterns:
            digits.append(code_patterns[segment])
        else:
            return []
    return digits

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    lines = [input().strip() for _ in range(N)]

    valid_code = []
    for line in lines:
        if '1' in line:
            code = decode_line(line)
            if code:
                valid_code = code
                break #다 같은 숫자라서 전체 다 탐색할 필요없음
    answer = 0
    for i in range(8): #8자리
        if i % 2 == 0: #짝수
            answer += valid_code[i] * 3
        else: #홀수
            answer += valid_code[i]
    
    if answer % 10 == 0: #올바를때
        answer = sum(valid_code)
    else: #아닐때
        answer = 0

    print(f'#{test_case} {answer}')