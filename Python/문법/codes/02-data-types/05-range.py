my_range_1 = range(5)
my_range_2 = range(1, 10)
print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1)) 
print(list(my_range_2))

# 주로 반복문과 함께 활용
for i in range(5):  # 다섯바퀴 돈다
    print(i)

for i in range(1, 10, 2): #간격 2씩 다섯바퀴
    print(i) 