items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

# 문자열
country = 'Korea'

for char in country:
    print(char)

# range
for i in range(5):
    print(i)

# dic
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)       # key만 출력됨
    print(my_dict[key])

# 리스트 - len 활용
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

# 중첩된 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)

# 중첩된 리스트  -- 이중 for문 중요
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    for item in elem:
        print(item)
