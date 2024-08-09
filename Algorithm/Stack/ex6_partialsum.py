def f(i, k, s, t):
    global cnt
    # 가지치기 생략한 경우
    # if i == k:
    #     if s == t:
    #         cnt += 1
    #         return

    # 가지치기
    if s> t:
        return
    elif s == t:
        cnt+=1
        return
    elif i == k:
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i],t)  # A[i] 포함
        bit[i] = 0
        f(i+1,k,s,t)  # A[i] 미포함

A = [1,2,3,4,5,6,7,8,9,10]
N = 10
key = 10
cnt = 0
bit = [0]*N
