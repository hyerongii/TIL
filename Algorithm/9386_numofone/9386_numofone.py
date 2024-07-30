
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    max_num = 0
    # 1이 연속할 수 있는 만큼의 리스트 생성 
    for num in range(1, N+1):
        window = [1] * num

        # window를 수열에 있는지 확인
        for i in range(N):
            if arr[i:i+num] == window:
                max_num += num
        
    print(f'#{test_case} {max_num}')