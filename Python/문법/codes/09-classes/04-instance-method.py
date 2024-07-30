class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 함수의 매개변수 이름
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요. {self.name}입니다.')

# 초기값 설정 필요! self, name 으로 했기 때문
person1 = Person('지민')

# 실제로 위와 아래는 동일함 하지만 파이썬에서는 위와 같은 단축형 호출 사용함
person1.greeting()
Person.greeting(person1)
