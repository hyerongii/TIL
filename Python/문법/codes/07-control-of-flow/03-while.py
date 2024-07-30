a = 0

while a < 3:
    print(a)
    a += 1

print('끝')

# 원하는 값을 입력하게 유도하는 곳에 while 쓰일 수 있다..!

number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')
