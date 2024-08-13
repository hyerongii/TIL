N = 10
q = [0] * N
front = -1
rear = -1

# 이 방법이 더 빠르게 처리 가능함
rear += 1  # enqueue(1)
q[rear] = 1
rear += 1
q[rear] = 2 # enqueue(2)
rear += 1 
q[rear] = 3 # enqueue(3)

front += 1 # dequeue()
print(q[front])
front += 1 # dequeue()
print(q[front])
front += 1 # dequeue()
print(q[front])

# 간단하지만 느리게 처리됨
q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))
print(q2.pop(0))