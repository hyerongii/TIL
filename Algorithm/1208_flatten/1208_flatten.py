import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump = int(input())
    arr = list(map(int, input().split()))

    for _ in range(dump):
        diff = max(arr) - min(arr)
        if diff <= 1:
            break
        arr[arr.index(max(arr))] = max(arr) - 1
        arr[arr.index(min(arr))] = min(arr) + 1
        
        diff = max(arr) - min(arr)

    print(f'#{test_case} {diff}')
