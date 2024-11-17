import sys
sys.stdin = open("input.txt", "r")

def flatten(heights):
    for i in range(max_dump):
        max_height = max(heights)
        min_height = min(heights)
        max_height_idx = heights.index(max_height)
        min_height_idx = heights.index(min_height)

        heights[max_height_idx] -= 1
        heights[min_height_idx] += 1

    return max(heights) - min(heights)

for test_case in range(1,11):
    max_dump = int(input())
    heights = list(map(int, input().split()))

    max_difference = flatten(heights)

    print(f'#{test_case} {max_difference}')