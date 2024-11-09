import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,11):
    origin_length = int(input()) #원본 암호문의 길이
    origin = list(input().split())
    num_command = int(input())
    commands = list(input().split())

    for i in range(len(commands)):
        if commands[i] == 'I':
            x = int(commands[i+1])
            y = int(commands[i+2]) 
            numbers = commands[i+3:i+3+y]
            start_index = x
            for i in range(len(numbers)):
                origin.insert(start_index+i, numbers[i])
         
    answer = []
    for i in range(10):
        answer.append(origin[i])

    print(f'#{test_case} {" ".join(map(str,answer))}')