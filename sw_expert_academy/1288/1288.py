import sys
sys.stdin = open('input.txt', 'r')

T = int(input())



def check_all_numbers_true(numbers):
    result = True
    for key, values in numbers.items():
        if values is False:
            result = False
            break
    return result
    #return all(numbers.values())

def check_numbers(digits,numbers):
    for digit in digits:
        numbers[digit] = True


for test_case in range(1,T+1):
    N = int(input())
    
    numbers = {i: False for i in range(10)}
    
    count = 0
    while not check_all_numbers_true(numbers): #False
        count += 1 
        
        current_N = N * count #ex) N = 1295 currnet_N = 2590
        digits = [int(digit) for digit in str(current_N)] #2,5,9,0
        check_numbers(digits, numbers)

    total = N * count
    
    print(f'#{test_case} {total}')