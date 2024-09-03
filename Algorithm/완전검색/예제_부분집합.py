arr = ["A", "B", "C", "D", "E"]  # 이중 최소 2명 이상의 친구 선정
n = len(arr)

def get_sub(tar):
  cnt = 0
  for i in range(n):
    if tar & 0x1:
      cnt += 1
      tar >>= 1
  return cnt

result = 0
for tar in range(0, 1 << n) : # range(0,8) # 전체 부분집합을 확인하겠다.
  if get_sub(tar) >= 2:
    result += 1
print(result)