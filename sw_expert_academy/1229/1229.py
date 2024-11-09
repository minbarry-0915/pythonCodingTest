import sys
sys.stdin = open('input.txt', 'r')         

for test_case in range(10):
    origin_length = int(input())
    origin = list(input().split())
    command_num = int(input())
    commands = list(input().split())

    i = 0
    while i < len(commands):
        if commands[i] == 'I':
            x = int(commands[i + 1])
            y = int(commands[i + 2])
            numbers = commands[i + 3: i + 3 + y]
            # x 위치 다음에 y개의 숫자를 한 번에 삽입
            origin[x:x] = numbers
            i += 3 + y
        elif commands[i] == 'D':
            x = int(commands[i + 1])
            y = int(commands[i + 2])
            # x 위치 다음부터 y개의 숫자를 슬라이싱으로 제거
            del origin[x: x + y]
            i += 3
        else:
            i += 1

    # 첫 10개의 숫자를 출력
    answer = origin[:10]
    print(f'#{test_case + 1} {" ".join(answer)}')
