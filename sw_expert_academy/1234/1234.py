import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1,11):
    N, password = input().split()

    while True:
        found = False
        for i in range(10):
            idx = password.find(str(i) * 2)
            
            if idx != -1:
                password = password[: idx] + password[idx + 2:]
                found = True
        
        if not found:
            break
        if password[0] == '0':
            password = password[1:]

    print(f'#{test_case} {password}')