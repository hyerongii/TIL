# find
text = 'banana'
print(text.find('a')) # 1
print(text.find('z')) # -1
print(text.find('ba')) # 0

# index
print(text.index('a')) # 1
#print(text.index('z')) # 찾고자 하는 인자가 없을 시 Error 남

# isupper/islower
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.islower()) # False
print(string2.islower()) # False

# isalpha
string1 = 'Hello'
string2 = '123'
print(string1.isalpha()) # True
print(string2.isalpha()) # False

# replace
text = 'Hello, world! world world'
new_text = text.replace('world', 'Python', 1)
print(new_text)

# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text) # 'Hello, world!'

# split
text = 'Hello, world!'
words = text.split(',')
print(words) # ['Hello', ' world!'] 공백은 생략 안됨

words2 = text.split()
print(words2) # ['Hello,', 'world!'] 공백을 기준으로 나눠짐

# join
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text)

# capitalize, title, upper, lower, swapcase
text = 'heLLo, woRld! world'
new_text1 = text.capitalize() # 맨 앞 글자만 대문자로 바꾸고 뒤는 다 소문자로 바꿔줌
new_text2 = text.title() # 공백 뒤 글자 대문자
new_text3 = text.upper() # 모두 다 대문자
new_text4 = text.swapcase() # 대문자 -> 소문자, 소문자 -> 대문자

print(new_text1) # Hello, world!
print(new_text2) # Hello, World!
print(new_text3) # HELLO, WORLD!
print(new_text4) # HEllO, WOrLD!


# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())
