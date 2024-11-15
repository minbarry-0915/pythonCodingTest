import sys
sys.stdin = open('input.txt','r')

T = 10



for test_case in range(1,T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    available = 0

    for i in range(2,N-2): # 첫번째, 마지막 두칸은 고려 x
        compare_buildings = buildings[i-2: i+3] #좌 우 두칸씩
        compare_buildings.remove(buildings[i])

        max_building = max(compare_buildings)
        if max_building < buildings[i]:
            available += buildings[i] - max_building

    print(f'#{test_case} {available}')