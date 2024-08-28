'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def search(node):
    if node != 0: # 그 node 값이 0이 아니라면
        print(node) # 전위순회면...
        search(tree[node][0]) # 왼쪽을 조사
        search(tree[node][1]) # 오른쪽을 조사


N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))

# tree 정보를 입력 할 수 있도록 하겠다.
# tree 리스트의 index 번호 -> 부모 노드의 번호
# tree[parent] 위치의 리스트의 0번째 - 왼쪽자식
# tree[parent] 위치의 리스트의 1번째 - 오른쪽 자식

tree = [[0, 0] for _ in range(N)] # 0번 노드 안쓸거임

for i in range(len(arr)): # 간선 정보 주어짐
    # 부모 자식 관계를 한번에 나타내고 싶음
    if not tree[arr[2*i]][0]:
        tree[arr[2*i]][0] = arr[2*i+1] 
    else:
        tree[arr[2*i]][1] = arr[2*i+1]

