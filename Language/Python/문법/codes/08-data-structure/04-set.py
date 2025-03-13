# 세트는 순서가 없음
# add
my_set = {'a', 'b', 'c', 1, 2, 3}  # {1, 2, 3, 'c', 4, 'b', 'a'} 순서 매번 달라짐
my_set.add(4)
print(my_set)
my_set.add(4) # 4 중복되지 않음
print(my_set)

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)

# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop() # 임의의 요소를 제거하고 반환. 규칙성 x
print(element)
print(my_set)

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
result = my_set.discard(10) # 없는 요소 제거하려고 했는데 error 없음
print(result) # None

# update(iterable)
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5]) # 1은 중복되어서 안들어가고 4, 5 만 들어감 순서는 없음
print(my_set)

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # set1 - set2 # {0, 2, 4}
print(set1.intersection(set2)) # set1 & set2 # {1, 3}
print(set1.issubset(set2)) # set1 <= set2 # False 
print(set3.issubset(set1)) # set3 <= set1 # True
print(set1.issuperset(set2)) # set1 >= set2 # False
print(set1.issuperset(set3)) # set1 >= set3 # True
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
