# pythonic 방법

# 10진수를
# 2진수로 변환. 주의 문자열..!
print(bin(10))
# 8진수
print(oct(10))
# 16진수
print(hex(10))

# 16진법 -> 10진법
print(int("F", base=16))
# 2진법 -> 10진법
print(int("1010", base=2))

print(bin(8)[2:]) # 4bit로 표기 -> 전처리
print(bin(1)[2:]).zfill(4) # 문자열에 남는 수 다 0 넣어줌

for i in range(16):               # 이거 사용하면 2진법으로 만들어주기 가능
    print(bin(i)[2:].zfill(4))  

# 만약 2진법: 16진법인 딕셔너리 만들고 싶다면
bin_to_hex = {}
for i in range(16):
    print(bin(i)[2:].zfill(4))
    print(hex(i)[2:])
    print(f'16진수 변환 소문자: {i:x}')
    print(f'16진수 변환 소문자: {i:X}')
    print(f'2진수 변환: {i:04b}')
    bin_to_hex[f'{i:04b}'] = f'{i:x}'
    # bin_to_hex[bin(i)[2:].zfill(4)] = hex(i)[2:]
print(bin_to_hex)

# 16진법: 2진법인 딕셔너리 만들고 싶다면
hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}
print(hex_to_bin)


# 2진수로 변환
def decimal_to_binary(n):
    binary_number = ""

    if n == 0:
        return "0"

    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remainder = n % 2
        binary_number = str(remainder) + binary_number
        n = n // 2

    return binary_number


# 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""

    if n == 0:
        return "0"

    # 0보다 클 때까지 16으로 나누면서 나머지를 정답에 추가
    while n > 0:
        remainder = n % 16
        hexadecimal_number = hex_digits[remainder] + hexadecimal_number
        n = n // 16

    return hexadecimal_number


# 예시: 10진수를 2진수와 16진수로 변환
decimal_num = 26
binary_num = decimal_to_binary(decimal_num)
hex_num = decimal_to_hexadecimal(decimal_num)

print(f"{decimal_num} - 2진수: {binary_num}")
print(f"{decimal_num} - 16진수: {hex_num}")

