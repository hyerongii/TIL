"""
1. 부분집합의 총 개수를 구해서, 해당 수까지 순차적으로 순회한다. ( 이유는 각 수의 비트를 구해서, 각 비트에 맞춰 부분집합을 구하기 위해서)
2. 부분 집합을 구하려는 리스트의 개수만큼 1을 left shift 하면서 비교한다.
3. shift 하면서 i의 비트 중 1인 애들을 고르고, 고른 모든 값들을 부분집합 목록에 집어넣는다.
"""
# arr 배열에서 모든 부분 집합을 생성하는 코드
arr = [1, 2, 3]
n = len(arr)  # 배열의 길이
subset_cnt = 2 ** n  # 생성 가능한 부분 집합의 총 개수

subsets = []  # 모든 부분 집합을 저장할 리스트
for i in range(subset_cnt):  # 모든 가능한 부분 집합을 생성하기 위한 반복문
    subset = []  # 현재 부분 집합을 저장할 리스트
    for j in range(n):  # 각 요소에 대해 포함 여부를 결정하기 위한 반복문
        if i & (1 << j):  # i의 j번째 비트가 1인지 확인
            subset.append(arr[j])
    subsets.append(subset)

print(subsets)
