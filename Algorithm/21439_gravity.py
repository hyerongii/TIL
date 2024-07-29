T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

# N개의 0을 가지고 있는 리스트 result 생성
    result = [0] * N
# 반복하면서 자기자신보다 작은 값들일 때 갯수를 셈
    for idx in range(N):
        count = 0
        for com in range(idx +1, N):
            if arr[idx] > arr[com]:
                count += 1
        result[idx] = count
    max_gravity = 0
# 최대값 찾기
    for num in range(len(result)):
        if result[num] > max_gravity:
            max_gravity = result[num]
    print(f'#{test_case} {max_gravity}')
