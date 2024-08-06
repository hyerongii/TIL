"""
버블정렬에 비해 교환횟수가 많다.
시간복잡도 : O(N^2) => 전체를 순회하면서 교환(N) <- 이 과정을 (N)번 해야함
안정성이 있다. ( 같은 키 값이 있을 경우에 그 순서가 유지됨)
"""
def bubble_sort(input_list):
    n = len(input_list)  # 리스트의 길이를 구하기

    for i in range(n):
        for j in range(0, n - i - 1):  # 마지막 i개 요소는 이미 정렬되어 있으므로 비교에서 제외
            if input_list[j] > input_list[j + 1]:  # 현재 요소가 다음 요소보다 큰 경우
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]  # 두 요소를 교환


num_list = [55, 7, 78, 12, 42]
bubble_sort(num_list)
print(num_list)  # [7, 12, 42, 55, 78]
