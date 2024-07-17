# 1. Positional Arguments (위치 인자 값)
def greet(name, age):
    print(f'안녕하세요. {name}님! {age}살이시군요.')    

greet('Harry', 20)
greet(20, 'Harry') # 가능하다. 위치인자는 아무 의미없음.

# 2. Default Argument Values (기본 인자 값)
def greet(name, age=20):
    print(f'안녕하세요. {name}님! {age}살이시군요.')   

greet('Bob')
greet('Charlie', 40)

# 3. Keyword Arguments (키워드 인자)
def greet(name, age):
    print(f'안녕하세요. {name}님! {age}살이시군요.')   

greet(name='Dave', age=30)
greet(age=30, name='Dave') # 순서 바뀌는 거는 된다
# greet(age=30, 'Dave') # 이건 안된다

# 4. Arbitrary Argument Lists (임의의 인자 목록)
def calculate_sum(*args):  # 임의의 인수할 때 보통 args 많이 씀
    print(args)
    # print(type(args))

calculate_sum(1,100,50000,30) # (1,100,50000,30) tuple 형태로 출력됨

def calculate_sum_position(params, *args):
    print(params,args)

calculate_sum_position(1,100,50000,30) # 1 (100, 50000, 30) 1은 위치인자, 뒤의 3개는 임의의 인자

# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30) # {'name': 'Eve', 'age': 30}

# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
