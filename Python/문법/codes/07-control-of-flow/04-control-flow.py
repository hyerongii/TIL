# break

for i in range(10):
    if i == 5:
        break        # for문 나오고 싶을 때
    print(i)

# continue

for i in range(10):
    if i % 2 == 0:
        continue     # 스킵하고 싶을 때
    else:
        print(i)

# pass

for i in range(10):
    pass              # 갑자기 생각 안날 때, 에러 방지로 pass 사용함

# break 예시 1 - "프로그램 종료 조건 만들기"
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number == -9999:    # 어떤 입력에서 강제 종료 하고 싶을 때
        print('프로그램을 종료합니다.')
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')


# break 예시 2 - "리스트에서 첫번째 짝수만 찾은 후 반복 종료하기"
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print(f'첫번째 짝수 {num}를 찾았습니다.')
        found_even = True
        break

#만약 짝수를 발견했다면 아래 구절 프린트 되지 않을것
if found_even == False:
    print('짝수를 찾지 못함')


# continue 예시 - "리스트에서 홀수만 출력하기"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
