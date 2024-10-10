
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input().strip())
    
    total = {
        '50000' : N // 50000,
        '10000' : (N % 50000) // 10000,
        '5000' : ((N % 50000) % 10000) // 5000,
        '1000' : (((N % 50000) % 10000) % 5000) // 1000,
        '500' : ((((N % 50000) % 10000) % 5000) % 1000) // 500,
        '100' : (((((N % 50000) % 10000) % 5000) % 1000) % 500) // 100,
        '50' : ((((((N % 50000) % 10000) % 5000) % 1000) % 500) % 100) // 50,
        '10' : ((((((((N % 50000) % 10000) % 5000) % 1000) % 500) % 100) % 50)) // 10
    }
    
    arr = []
    arr.append(str(total['50000']))
    arr.append(str(total['10000']))
    arr.append(str(total['5000']))
    arr.append(str(total['1000']))
    arr.append(str(total['500']))
    arr.append(str(total['100']))
    arr.append(str(total['50']))
    arr.append(str(total['10']))
    
    print(f'#{test_case}');
    print(' '.join(arr))    
    # ///////////////////////////////////////////////////////////////////////////////////