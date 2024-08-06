# 모든 배열 원소에 접근하기
def f(i,N):
    if i == N:  # 중단하는 경우를 앞에 써주기
        return
    else:
        print(arr[i])
        f(i+1, N)
        return  # 생략해도 작동 잘 됨

arr = [1,2,3,4]
print(f(0,4))

# 배열에 v가 있으면 1, 없으면 0을 리턴

def ff(i,N,v): # v: 찾는 값
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return ff(i+1, N, v)

print(ff(0,4,3))


