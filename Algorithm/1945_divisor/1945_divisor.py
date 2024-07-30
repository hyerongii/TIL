import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    divisor_list = [2, 3, 5, 7, 11]
    count_list = [0] * 5      # a, b, c, d, e 순

    while N != 1:
        for divisor in divisor_list:
            if N % divisor == 0:
                N //= divisor
                count_list[divisor_list.index(divisor)] += 1
    
    print(f'#{test_case} {" ".join(list(map(str, count_list)))}')