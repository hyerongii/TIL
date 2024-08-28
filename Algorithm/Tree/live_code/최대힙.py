'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''


# 최대힙
# 삽입 -> 마지막에 삽입 -> 자리 찾아가기
def enq(n):
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지) - len 연산 피하기 위해서
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모>자식 비교를 위해
    p = c//2    # 부모번호 계산
    while p >= 1 and h[p] < h[c]:   # 부모가 있는데, 더 작으면 # 제자리를 찾거나 루트일때 멈춘다
        h[p], h[c] = h[c], h[p]  # 교환
        c = p
        p = c//2

# 삭제 -> 마지막 노드 값을 루트에 복사 -> 마지막 노드 삭제 -> 자리 찾기
def deq():
    global last
    tmp = h[1]   # 루트의 키값 보관 # 최종값은 리턴해주고
    h[1] = h[last] # 마지막에 있는걸 그 위치로 이동
    last -= 1 
    p = 1           # 새로 옮긴 루트
    c = p*2  # 왼쪽자식이랑 비교
    while c <= last:  # 자식이 있으면
        if c+1 <= last and h[c] < h[c+1]: # 오른쪽자식이 있고 더 크면
            c += 1
        if h[p] < h[c]: # 비교 후 swap
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp


N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

h = [0]*(N+1)   # 최대힙 (완전이진트리 보장 - 일차원리스트 구현 - N노드의 자식은 N*2 N*2+1)
last = 0        # 힙의 마지막 노드 번호

for num in arr:
    enq(num)

print(h)

while last > 0:
    print(deq(), end=' ')
