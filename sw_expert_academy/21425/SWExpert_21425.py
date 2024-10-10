'''
C, C++, Python, Java 등의 언어에는 += 연산자가 있다. 정수형 변수 x, y가 있을 때 “x += y”를 하면 x에 저장된 값이 (기존에 x에 저장되어 있던 값) + (기존에 y에 저장되어 있던 값)으로 바뀐다.

현재 x에 저장된 값은 A, y에 저장된 값은 B이다. 당신은 “x += y” 또는 “y += x” 연산을 원하는 순서대로 원하는 만큼 수행하여, x나 y 둘 중 하나 이상에 저장된 값이 N 초과가 되게 하려고 한다. 연산을 합쳐서 최소 몇 번 수행해야 하는지 계산하는 프로그램을 작성하라.

# 입력
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스는 한 개의 줄로 이루어진다. 각 줄에는 세 개의 정수 이 공백 하나씩을 사이로 두고 주어진다.
테스트 케이스의 개수는 600,000개 이상으로 상당히 많음에 유의하라.

# 출력
각 테스트 케이스마다, 한 줄에 하나씩 x나 y 둘 중 하나 이상에 저장된 값이 N 초과가 되게 하기 위해 “x += y”, “y += x” 연산을 최소 몇 번 수행해야 하는지 출력한다.
'''


# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    x,y,N = map(int, input().split())
    count = 0
    while x <= N and y <= N:
        if x <= y:
            x += y
        else:
            y += x
        count += 1
        
    print(count);    
    # ///////////////////////////////////////////////////////////////////////////////////
'''
출처 : https://swexpertacademy.com/
'''