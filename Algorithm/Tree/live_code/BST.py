'''
7
3 5 1 2 7 4 -5
'''
# 연결리스트로 생성, 좌우는 비우고 중간값만 데이터
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    # 최상위 root만 관리
    def __init__(self):
        self.root = None

    def insert(self, key):
        # 아무 것도 없다면 그냥 삽입
        if self.root is None:
            self.root = Node(key)
        else:
            # 값 있다면 자리를 찾아서 삽입
            self._insert(self.root, key)

    def _insert(self, node, key):
        # 작으면 왼쪽 고려
        if key < node.key:
            # 아무것도 없으면 그냥 삽입
            if node.left is None:
                node.left = Node(key)
            # 값 있으면 재귀로 한번 더 탐색
            else:
                self._insert(node.left, key)
        # 크면 우측 고려
        else:
            # 아무것도 없으면 그냥 삽입
            if node.right is None:
                node.right = Node(key)
            # 값 있으면 재귀로 한번 더 탐색
            else:
                self._insert(node.right, key)

    # 루트면 바로 찾기
    def search(self, key):
        return self._search(self.root, key)

    # node: 현재바라보고 있는 node, key: target
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        # 작다면 왼쪽을
        if key < node.key:
            return self._search(node.left, key)
        # 크다면 오른쪽을
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
