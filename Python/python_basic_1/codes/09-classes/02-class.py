# 클래스 정의 : 속성과 메서드로 이루어져 있다.
class Person:
    blood_color = 'red' # blood_color 는 속성

    def __init__(self, name): # __init__, singing 메서드
        self.name = name
    
    def singing(self):
        return f'{self.name}가 노래합니다.'

    # 행동을 주도적으로 하는 것은 클래스에서 만들어진 인스턴스

# 인스턴스 생성
singer1 = Person('iu')

# (인스턴스) 메서드 호출
print(singer1.singing())

# 속성(변수) 접근
print(singer1.blood_color)

#인스턴스 속성(변수)
print(singer1.name)