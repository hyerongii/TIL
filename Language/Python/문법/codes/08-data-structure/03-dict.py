# clear
# person = {'name': 'Alice', 'age': 25}
# person.clear()
# print(person)

# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) # Alice
print(person.get('country')) # None
#print(person['country'])  # key error
print(person.get('country', 'Unknown')) # Unknown
print(person)

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys()) # 반복 돌릴 수 있음
for item in person.keys():
    print(item)

# values
person = {'name': 'Alice', 'age': 25}
print(person.values()) # 반복 돌릴 수 있음
for item in person.values(): 
    print(item)

# items
person = {'name': 'Alice', 'age': 25}
print(person.items()) # 키와 벨류가 함께 튜플로 묶여서 나옴 # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items(): # key, value 를 함께 매개변수로 사용하기
    print(key)
    print(value)

# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 키를 제거하고 연결되었던 값 25 반환
print(person) # {'name': 'Alice'}
print(person.pop('country',None)) # None
#print(person.pop('country')) # error

# setdefault
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country','KOREA'))
print(person)

# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person) # 기존 키에 덮어서 쓰임
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age=50) # 새로운 key, value 삽입 가능
print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female'}

person.update(country='KOREA')
print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}

