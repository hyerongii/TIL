# super 사용 전
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id



# super 사용 예시 - 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id, gpa):
        super().__init__(name, age, number, email) # self 는 안넣어도 된다.
        self.student_id = student_id
        self.gpa = gpa


# super 사용 예시 - 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 호출한다.
        self.value_c = 'Child'
        # self.value_a 생기고 self.value_c 생긴다.

child1 = Child()
print(child1.value_a)
print(child1.value_c)
# print(child1.value_b) # error 발생

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 호출한다.
        ParentB.__init__() # 만약 parentB 호출하고 싶다면,,
        self.value_c = 'Child'
        # self.value_a 생기고 self.value_c 생긴다.