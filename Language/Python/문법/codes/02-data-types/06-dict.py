my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {               # 나타낼 수 있음. 인덱스가 없음. 순서가 없음.
    'apple': 12, 
    'list': [1, 2, 3]
}
print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}


my_dict = {'apple': 12, 'list': [1, 2, 3]}

# !!! 딕셔너리는 키에 접근해 값을 얻어냄
print(my_dict['apple']) # 12

# 추가
my_dict['banana'] = 50 # 없는 키를 값을 할당해 추가하면 추가됨
print(my_dict)

# 변경
my_dict['banana'] = 1000 # 있는 키의 값 할당하면 값이 변경됨
print(my_dict)
