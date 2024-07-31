import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 9개 행을 10번의 테스트 케이스 만큼 받기
    arr = []
    count_num = 0
    for i in range(9):
        arr.append(list(map(int, input().split())))

    reverse_arr = [[0] * 9 for _ in range(9)]

    # 1 x 9 window 만큼 순회하면서 겹치는 값 찾기 - 중복된 값 찾는거 set 써보기
    for i in range(9):
        for j in range(9):
            reverse_arr[j][i] = arr[i][j]
            if arr[i].count(arr[i][j]) > 1:
                count_num += 1

    # 9 x 1 window 만큼 순회하면서 겹치는 값 찾기 - zip 써도 될듯
    for i in range(9):
        for j in range(9):
            if reverse_arr[i].count(reverse_arr[i][j]) > 1:
                count_num += 1

    di = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dj = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    # 3 x 3 window 만큼 순회하면서 겹치는 값 찾기

    divisor_arr = []
    for num in range(9):
        if num % 3 == 0:
            divisor_arr.append(num)

    for i in divisor_arr:  # [0,3,6]
        for j in divisor_arr:
            three_n_arr=[]
            for k in range(9):
                three_n_arr.append(arr[i+di[k]][j+dj[k]])
            for l in range(9):
                if three_n_arr.count(three_n_arr[l]) > 1:
                    pass
                    count_num += 1

    if count_num > 0:
        result = 0
    else:
        result = 1

    print(f'#{test_case} {result}')


