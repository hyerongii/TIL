# 3개의 선택된 값을 저장할 리스트 초기화
selected = [0] * 3
"""
- knapsack 문제

[1, 2, 3] 에서 선택하냐, 안 하냐의 문제로 부분집합을 구할 수 있음
이를 for loop 로 구현하면 아래와 같음 
"""
# i, j, m은 각각 첫 번째, 두 번째, 세 번째 선택된 값을 나타냄
for i in range(2):
    selected[0] = i  # 첫 번째 값 설정
    for j in range(2):
        selected[1] = j  # 두 번째 값 설정
        for m in range(2):
            selected[2] = m  # 세 번째 값 설정
            subset = []  # 부분 집합을 저장할 리스트 초기화
            for n in range(3):  # selected 리스트의 각 요소에 대해 반복
                if selected[n] == 1:  # 요소가 1인 경우
                    subset.append(n+1)  # 부분 집합에 요소 추가 (1부터 시작하도록 조정)
            print(subset)  # 현재 부분 집합 출력
