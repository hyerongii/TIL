# 1 ~ N 까지의 수를 조합해 만들 수 있는 M자리수 출력

def backtracking():
    if len(answer) == M: # 탈출코드
        print("".join(map(str, answer)))
        return
    for i in range(1, N+1):
        if i not in answer: # 안들어있으면
            answer.append(i) # 넣고
            backtracking() # 다시 반복
            answer.pop() # 다 구하면 그 전으로 이동

N = 4
M = 3
answer = []
backtracking()