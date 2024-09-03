# 주사위 던지기. 주사위 N개를 던져서 나올 수 있는 모든 조합 출력
# N= 3 일때

arr = list(range(1, 7))
path = []

n = 3
def run(lev, start):
  if lev == n:
    print(path)
    return

  for i in range(start, 6):
    path.append(arr[i])
    run(lev+1, i)
    path.pop()

run(0, 0)