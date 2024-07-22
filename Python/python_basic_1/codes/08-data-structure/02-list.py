# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
print(my_list.append(4))

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)
#my_list.extend(5) # Error (5는 eterable 아니기 때문)

# insert
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) #[1, 5, 2, 3]

# remove
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list) # [1, 3]

# pop (반환 값 있음)
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop() # 마지막 항목을 제거
item2 = my_list.pop(0)
print(item1)
print(item2)
print(my_list)

# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)

# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1

# count
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count) # 3

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list) 

my_list.sort(reverse=True)
print(my_list)


# sort(내림차순 정렬)
