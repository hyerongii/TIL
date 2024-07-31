# Classes
## 객체지향 프로그래밍

### 개요
#### 절차 지향 프로그래밍 `Procedural Programming`
- 프로그램을 '데이터'와 '절차'로 구성하는 방식의 프로그래밍 패러다임

#### 절차 지향 프로그래밍 특징

- "데이터"와 해당 데이터를 처리하는 "함수(절차)"가 분리되어 있으며, 함수 호출의 흐름이 중요
- 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행
- 실제로 실행되는 내용이 무엇이 무엇인가가 중요
- 데이터를 다시 재사용하거나 하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식

![image](https://github.com/ragu6963/TIL/assets/32388270/cc0db5a1-8200-409b-8b90-c42ea7823c71)

#### 소프트웨어 위기 (Software Crisis)
- 하드웨어의 발전으로 컴퓨터 계산 용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격

![image](https://github.com/ragu6963/TIL/assets/32388270/e251d24f-781d-46ca-b6dd-56f1c2c8e9d1)

#### 객체 지향 프로그래밍 `Object Oriented Programming`

- 데이터와 해당 데이터를 조장하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임

#### 절차 지향 vs 객체 지향

- 절차 지향
    - 데이터와 해당 데이터를 처리하는 함수(절차)가 분리
    - 함수 호출의 흐름이 중요

- 객체 지향 
    - 데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음
    - 객체 간 상호작용과 메시지 전달이 중요

## 객체
### 개요
#### 클래스 `Class`

- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공

#### 객체 'Object'

- 클래스에서 정의한 것을 토대로 메모리에 할당된 것
- <span style='color:red;'>'속성'</span>과 <span style='color:red;'>'행동'</span>으로 구성된 모든 것

#### 객체 예시
![image](https://github.com/ragu6963/TIL/assets/32388270/1e728c44-90e5-4acc-99bb-a4ab1998c3b9)

#### 클래스와 객체
- 클래스로 만든 객체를 <span style='color:red;'>인스턴스</span> 라고 부름
    ![image](https://github.com/ragu6963/TIL/assets/32388270/f3447cce-fcab-4f66-81da-3047c77df12b)

- 변수 name의 타입은 str 클래스다.
- 변수 name은 <span style='color:red;'>str 클래스의 인스턴스</span>이다.
- 우리가 사용해왔던 <span style='color:red;'>데이터 타입은 사실 모두 클래스</span>였다.

    ```py
    name = 'Alice'
    print(type(name)) # <class 'str'>
    ```

- 결국 문자열 타입의 변수는 str 클래스로 만든 인스턴스다.

    ```py
    print(help(str))

    """
    class str(object)
     |  str(object='') -> str
     |  str(bytes_or_buffer[, encoding[, errors]]) -> str
     |
     |  Create a new string object from the given object. If encoding or
     |  errors is specified, then the object must expose a data buffer
     |  that will be decoded using the given encoding and error handler.
     |  Otherwise, …
    """
    ```
#### 인스턴스와 메서드

```py
“hello”.upper()

"""
문자열.대문자로()

객체.행동()

인스턴스.메서드()
"""
```

```py
[1, 2, 3].sort()

"""
리스트.정렬해()

객체.행동()

인스턴스.메서드()
"""
``` 
> 하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.

- 123, 900, 5는 모두 `int`의 인스턴스
- 'hello', 'bye'는 모두 `string`의 인스턴스
- [232, 89, 1], [] 은 모두 `list`의 인스턴스

#### 객체(object)의 특징

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

    ![image](https://github.com/ragu6963/TIL/assets/32388270/dfed70e3-bc37-45ef-988a-b6becc4806b8)

## 클래스
### 개요
#### 클래스 `Class`
- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공

#### 클래스 정의
- class 키워드
- 클래스 이름은 파스칼 케이스(Pascal Case) 방식으로 작성

    ```py
    class MyClass:
        pass
    ```
#### 인스턴스 생성 및 활용

```py

# 인스턴스 생성
iu = Person()

# 메서드 호출
iu.메서드()

# 속성(변수) 접근
iu.attribute

# 클래스 정의 
class Person:
    blood_color = 'red'

    def __init__(self, name):
        self.name = name
    
    def singing(self):
        return f'{self.name}가 노래합니다'

# 인스턴스 생성
singer1 = Person('iu')

# 메서드 호출
print(singer1.singing())  # iu가 노래합니다.

# 속성(변수) 접근
print(singer1.blood_color)  # red
```

### 클래스 구성요소
1. 생성자 함수
    - 객체를 생성할 때(인스턴스를 만들때) **자동으로 호출**되는 특별한 메서드 (매직메서드)
    - `__init__`이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
    - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정

    ```python
        class Person:
        blood_color = 'red'
        
        def __init__(self, name):
            self.name = name

        def singing(self):
            return f'{self.name}가 노래합니다.’
        

    # 인스턴스 생성
    singer1 = Person('iu')
    ```

2. 인스턴스 변수
    - **인스턴스(객체)마다 별도로 유지**되는 변수
    - 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨

    ```py
    class Person:
        blood_color = 'red'
        
        def __init__(self, name):
            self.name = name

        def singing(self):
            return f'{self.name}가 노래합니다.’


    singer1 = Person('iu')
    
    # 인스턴스 변수
    print(singer1.name)
    ```

3. 클래스 변수
    - 클래스 내부에 선언된 변수
    - 클래스로 생성된 모든 인스턴스들이 공유하는 변수

    ```py
    class Person:
        blood_color = 'red'
        
        def __init__(self, name):
            self.name = name

        def singing(self):
            return f'{self.name}가 노래합니다.’


    singer1 = Person('iu')

    # 클래스 속성(변수) 접근
    print(singer1.blood_color)

    ```

4. 인스턴스 메서드
    - 각각의 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행

    ```py
    class Person:
        blood_color = 'red'

        def __init__(self, name):
            self.name = name

        def singing(self):
            return f'{self.name}가 노래합니다.'


    singer1 = Person('iu')

    # 인스턴스 메서드 호출
    print(singer1.singing())
    ```

### 인스턴스 변수와 클래스 변수
#### 클래스 변수 활용

- 가수가 몇 명인지 확인하고 싶다면?
    - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정할 수 있음
    ```py
    class Person:
        count = 0
        
        def __init__(self, name):
            self.name = name
            Person.count += 1
        
        
    person1 = Person('iu')
    person2 = Person('BTS')
        
    print(Person.count)  # 2
    ```

#### 클래스 변수와 인스턴스 변수
- 클래스 변수를 변경할 때는 항상 <span style='color:red;'>클래스.클래스변수</span> 형식으로 변경

- 예시 1
    ```py
    class Circle:
        pi = 3.14

        def __init__(self, r):
            self.r = r

    c1 = Circle(5)
    c2 = Circle(10)
    print(Circle.pi)
    print(c1.pi)
    print(c2.pi)
    ```

- 예시 2

    ```py
    
    class Circle:
        pi = 3.14

        def __init__(self, r):
            self.r = r 


    c1 = Circle(5)
    c2 = Circle(10)

    Circle.pi = 5  # 클래스 변수 변경
    print(Circle.pi)  # 5
    print(c1.pi)  # 5
    print(c2.pi)  # 5 
    ```

- 예시 3 

    ```py
    
    class Circle:
        pi = 3.14

        def __init__(self, r):
            self.r = r 


    c1 = Circle(5)
    c2 = Circle(10)
    c2.pi = 5  # 인스턴스 변수 변경
    
    print(Circle.pi)  # 3.14 (클래스 변수)
    print(c1.pi)  # 3.14 (클래스 변수)
    print(c2.pi)  # 5 (새로운 인스턴스 변수가 생성됨)
    ```
## 메서드
### 개요
#### 메서드 종류

- 인스턴스 메서드
- 클래스 메서드
- 정적 메서드

### 인스턴스 메서드
#### 인스턴스 메서드 `instance method`

- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
- 인스턴스의 상태를 조작하거나 동작을 수행

#### 인스턴스 메서드 구조
- 클래스 내부에 정의되는 메서드의 기본
- 반드시 첫 번째 매개변수로 <span style='color:red;'>**인스턴스 자신(self)**</span>을 전달받음
- self는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능하지만 다른 이름을 사용하지 않을 것을 강력히 권장

```py
class MyClass
    def instance_method(self, arg1, ...):
        pass

```

#### self 동작 원리
- upper 메서드를 사용해 문자열 'hello'를 대문자로 변경하기
    ```py
    'hello'.upper()
    ```
- 하지만 실제 파이썬 내부 동작은 다음과 같이 진행됨
    ```py
    str.upper('hello')
    ```
- str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것
- <span style='color:red;'>인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기 자신인 이유</span>

- `'hello'.upper()` 은 `str.upper('hello')`를 객체 지향 방식의 메서드로 호출하는 표현 (`단축형 호출`)

- ‘hello’라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적 표현

#### 생성자 메서드 `constructor method'
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정

#### 생성자 메서드 구조

```py
class Person:
    def __init__(self, name):
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요. {self.name}입니다.')

person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.
```

### 클래스 메서드
#### 클래스 메서드 `class method`

- 클래스가 호출하는 메서드
- 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

#### 클래스 메서드 구조

- `@classmethod` **데코레이터**를 사용하여 정의
- 호출 시, 첫번째 인자로 호출하는 클래스(cls)가 전달됨
- cls는 매개변수 이름일 뿐이며 다른 이름으로 설정 가능 하지만 다른 이름을 사용하지 않을 것을 강력히 권장

```py
class MyClass:
    
    @classmethod
    def class_method(cls, arg1, ...):
        pass

```

### 스태틱 메서드
#### 스태틱(정적) 메서드 `static method`

- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
- 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용

#### 스태틱 메서드 구조

- @staticmethod 데코레이터를 사용하여 정의
- 호출 시 필수적으로 작성해야 할 매개변수가 없음
- 즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용

    ```py
    class MyClass:
        
        @staticmethod
        def static_method(arg1, ...):
            pass
    ```

#### 스태틱 메서드 예시

- 단순히 문자열을 조작하는 기능을 제공하는 메서드 예시

    ```py
    class StringUtils:
        @staticmethod
        def reverse_string(string):
            return string[::-1]

        @staticmethod
        def capitalize_string(string):
            return string.capitalize()


    text = 'hello, world'

    reversed_text = StringUtils.reverse_string(text)
    print(reversed_text) # dlrow ,olleh

    capitalized_text = StringUtils.capitalize_string(text)
    print(capitalized_text) # Hello, world

    ```

### 메서드 정리
#### 메서드 정리
- 인스턴스 메서드  
    - 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행
    - self 꼭사용, 인스턴스만 사용
- 클래스 메서드
    - 인스턴스의 상태에 의존하지 않는 기능을 정의
    - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
    - @ 데코레이터 사용, cls 사용
- 스태틱 메서드
    - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행
    - @ 데코레이터 사용

#### 누가 어떤 메서드를 사용해야 할까
- 클래스가 사용해야 할 것
    - 클래스 메서드
    - 스태틱 메서드

- 인스턴스가 사용해야 할 것
    - 인스턴스 메서드

- 예시 클래스로 클래스와 인스턴스가 각각 모든 메서드를 호출해보기

```py
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance)) # 사용금지
print(MyClass.class_method()) 
print(MyClass.static_method()) 

# 인스턴스가 할 수 있는 것
print(instance.instance_method())
print(instance.class_method()) # 사용금지
print(instance.static_method()) # 사용금지
```

#### 클래스가 할 수 있는 것
- 클래스는 모든 메서드를 호출 할 수 있음
- <span style='color:red;'>하지만 클래스는 클래스 메서드와 스태틱 메서드만 사용하도록 한다</span>

#### 인스턴스가 할 수 있는 것
- 인스턴스는 모든 메서드를 호출 할 수 있음
- <span style='color:red;'>하지만 인스턴스는 인스턴스 메서드만 사용하도록 한다</span>

#### `할 수 있다 != 써도 된다`
- 각자의 메서드는 OOP 패러다임에 따라 명확한 목적에 맞게 설계된 것이기 때문에 클래스와 인스턴스 각각 올바른 메서드만 사용한다.

## 상속
### 개요
#### 상속 `Inheritance`

- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

#### 상속이 필요한 이유

1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
    - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음

2. 계층 구조 
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음

3. 유지 보수의 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐 
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최고화 할 수 있음

### 클래스 상속
#### 상속 없이 구현 하는 경우 (1/2)
- 학생/교수 정보를 나타내기 어려움

    ```py
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')


    s1 = Person('김학생', 23)
    s1.talk() # 반갑습니다. 김학생입니다.

    p1 = Person('박교수', 59)
    p1.talk() # 반갑습니다. 박교수입니다.
    ```
- 교수/학생 클래스로 분리했지만 메서드가 중복으로 정의될 수 있음

    ```py
    class Professor:
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department

        def talk(self): # 중복
            print(f'반갑습니다. {self.name}입니다.')

    class Student:
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa

        def talk(self): # 중복
            print(f'반갑습니다. {self.name}입니다.')
    ```
#### 상속을 사용한 계층구조 변경

![image](https://github.com/ragu6963/TIL/assets/32388270/ecdca0f0-47ce-4afc-853d-fa0d4575b458)

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.
```

### 다중 상속
#### 다중 상속 정의
- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 <span style='color:crimson;'>상속 순서에 의해 결정됨</span>

#### 다중 상속 예시

```py
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XY  # 아빠 먼저 상속 받아서 이렇게 됨
```

#### 다이아몬드 문제

![Diamond](https://i.ibb.co/b23YqZT/440px-Diamond-inheritanc.png)

- 두 클래스 B와 C가 A에서 상속되고 클래스 D가 B와 C 모두에서 상속될 때 발생하는 모호함
- B와 C가 재정의한 메서드가 A에 있고 D가 이를 재정의하지 않은 경우라면
- D는 B의 메서드 중 어떤 버전을 상속하는가? 아니면 C의 메서드 버전을 상속하는가?

#### 파이썬에서의 해결책

- MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록을 생성
- 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음
- 그래서, 속성이 D에서 발견되지 않으면, B에서 찾고, 거기에서도 발견되지 않으면, C에서 찾고, 이런 식으로 진행됨

    ```python
    class D(B, C):
        pass
    ```

#### MRO (Method Resolution Order)

- 메서드 결정 순서

#### `super()`

- 부모 클래스 객체를 반환하는 내장 함수
- 다중 상속시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출

#### super() 사용 예시 (단일 상속)

- 사용 전

    ```py
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
    ```

- 사용 후

    ```py
    class Person:
        def __init__(self, name, age, number, email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email


    class Student(Person):
        def __init__(self, name, age, number, email, student_id):
            # Person의 init 메서드 호출
            super().__init__(name, age, number, email)
            self.student_id = student_id

    ```

    ```python
    class ParentA:
        def __init__(self):
            self.value_a = 'ParentA'

        def show_value(self):
            print(f'Value from ParentA: {self.value_a}')


    class ParentB:
        def __init__(self):
            self.value_b = 'ParentB'

        def show_value(self):
            print(f'Value from ParentB: {self.value_b}’)


    class Child(ParentA, ParentB):
        def __init__(self):
            super().__init__() # ParentA 클래스의 __init__ 메서드 호출
            self.value_c = 'Child’

        def show_value(self):
            super().show_value() # ParentA 클래스의 show_value 메서드 호출
            print(f'Value from Child: {self.value_c}')

    child = Child()
    child.show_value()
    ```
#### `mro()` 사용 예시

- 다이아몬드 구조

  ```python
  class A:
      def __init__(self):
          print('A Constructor')

  class B(A):
      def __init__(self):
          super().__init__()
          print('B Constructor')

  class C(A):
      def __init__(self):
          super().__init__()
          print('C Constructor')
          
  class D(B, C):
      def __init__(self):
          super().__init__()
          print('D Constructor')

  print(D.mro())

    # 결과
    # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
  ```

#### MRO가 필요한 이유
- 부모 클래스들이 여러번 액세스 되지 않도록, 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고, 각 부모를 오직 한 번만 호출하고, 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성

> 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도움

> 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상

#### super의 2가지 사용 사례

1. 단일 상속 구조
    - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게 만들 수 있음
    - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요

2. 다중 상속 구조 
    - MRO를 따른 메서드 호출
    
    - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지

## 참고
### 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 <span style='color:red;'>독립적인</span> 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색

    ![image](https://github.com/ragu6963/TIL/assets/32388270/f1476ead-aff8-47ac-9118-b1e8095751e0)

    ```py
    # Person 정의
    class Person:
        name = 'unknown'

        def talk(self):
            print(self.name)


    p1 = Person()
    p1.talk()  # unknown
    """
    p1은 인스턴스 변수가 정의되어 있지 않아
    클래스 변수(unknown)가 출력됨
    """

    # p2 인스턴스 변수 설정 전/후
    p2 = Person()
    p2.talk()  # unknown
    p2.name = 'Kim'
    p2.talk()  # Kim
    """
    p2는 인스턴스 변수가 정의되어
    인스턴스 변수(Kim)가 출력됨
    """

    print(Person.name)  # unknown
    print(p1.name)  # unknown
    print(p2.name)  # Kim
    """
    Person 클래스의 값이 Kim으로 변경된 것이 아닌
    p2 인스턴스의 이름 공간에 name이 Kim으로 저장됨
    """
    ```

#### 독립적인 이름공간을 가지는 이점
- 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능

- 객체 지향 프로그래밍의 중요한 특성 중 하나로, <br>클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
- 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 <br>서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음
- 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌

### 매직 메서드 
- 특별한 인스턴스 메서드
- 특정 상황에 자동으로 호출되는 메서드
- Double underscore(`__`)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
    - 스페셜 메서드 혹은 매직 메서드라고 불림
- 예시
    ```python
    __str__(self)
    __len__(self)__
    __lt__(self, other)
    __le__(self, other)
    __eq__(self, other)
    __gt__(self, other)
    __ge__(self, other)
    __ne__(self, other)
    ```

#### 매직 메서드 예시
- `__str__(self)`
  - 내장함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경

```python
class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'원의 반지름: {self.r}'
    
c1 = Circle(10)
c2 = Circle(1)

print(c1) # 원의 반지름: 10
print(c2) # 원의 반지름: 1
```

### 데코레이터 (Decorator)
- 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

#### 데코레이터 정의
```python
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper
```

#### 데코레이터 사용

```python
@my_decorator
def my_function():
    print('원본 함수 실행')
my_function()

"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""
```
#### 절차 지향과 객체 지향은 대조되는 개념이 아니다
- 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해<br>
객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임 

