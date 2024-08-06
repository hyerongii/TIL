"""
버블정렬에 비해 교환횟수가 적다.
시간복잡도 : O(N^2) => 최소값을 찾기 위해 순회(N) , 한 칸씩 전진하면서 순회(N)
안정성이 없다.
"""
def selection_sort(input_list):
    n = len(input_list)  # 리스트의 길이

    for i in range(n - 1):  # 리스트 순회 (n-1 인 이유는 마지막 직전까지 순회한 경우, 이미 정렬이 완료된 상태이기 때문에)
        min_val = i  # 현재 위치를 최소값으로 가정

        for j in range(i + 1, n):  # 현재 위치 이후의 요소들에 대해 반복 ( 이유: 이미 앞쪽은 최소값들로 정렬한 상태이기 때문에)
            if input_list[j] < input_list[min_idx]:  # 현재 요소가 최소값보다 작은 경우
                min_idx = j  # 최소값 인덱스 갱신

        # 최소값과 현재 위치(i)의 요소를 교환
        # 결국 리스트 전체에서 최소값을 찾아서 맨 앞과 교환하고,
        # 이 후에 맨 앞을 제외한 목록에서 최소값을 찾아서 2번째와 교환하는 방식을 반복
        input_list[i], input_list[min_idx] = input_list[min_idx], input_list[i]


num_list = [64, 25, 10, 22, 11]
selection_sort(num_list)
print(num_list)  # [10, 11, 22, 25, 64]
