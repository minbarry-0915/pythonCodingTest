import sys
sys.stdin = open('input.txt','r')

T = 10



for test_case in range(1,T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    count = 0
    for i in range(2, N-2):
        compare_building = buildings[i - 2 : i + 3]
        compare_building.remove(buildings[i])
        max_building = max(compare_building)
        if max_building < buildings[i]:
            count += buildings[i] - max_building

    print(f'{test_case} {count}')