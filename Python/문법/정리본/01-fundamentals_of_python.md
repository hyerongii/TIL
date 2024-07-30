# Fundamentals of Python 
## 파이썬

### 파이썬 소개
#### 파이썬의 사용성과 인기

https://www.jetbrains.com/ko-kr/lp/devecosystem-2023/

#### 파이썬을 사용하는 이유

- 쉽고 간결한 문법
  - 읽기 쉽고 쓰기 쉬운 문법을 가지고 있어 쉽게 배우고 활용 할 수 있음

- 파이썬 커뮤니티의 지원
  - 세계적인 규모의 풍부한 온라인 포럼 및 커뮤니티 생태계

- 광범위한 응용 분야
  - 웹 개발, 데이터 분석, 인공지능, 자동화 스크립트 등 다양한 분야에서 사용

#### 알고리즘에 구현에 유리한 Python -> 코딩테스트에 유리

- 직관적인 문법
  - 복잡한 논리 구조의 알고리즘을 이해하고 구현하기에 쉬움

- 강력한 표준 라이브러리
  - 다양한 알고리즘 구현에 필요한 도구를 제공

- 빠른 프로토타이핑
  - 알고리즘을 빠르게 테스트하고 수정할 수 있음

### 파이썬 실행
#### 파이썬 프로그램이 실행되는 법

- 컴퓨터는 기계어로 소통하기 때문에 사람이 기계어를 직접 작성하기 어려움

    ![image](https://github.com/ragu6963/TIL/assets/32388270/0c62ec2c-6dbe-463f-b95d-17dc1d15bc62)
    
- 인터프리터가 사용자의 명령어를 운영체제가 이해하는 언어로 바꿈

    ![image](https://github.com/ragu6963/TIL/assets/32388270/6318332e-9c76-4c2b-b183-21280b338b8a)

#### 파이썬 인터프리터를 사용하는 2가지 방법
1. shell 이라는 프로그램으로 한 번에 한 명령어 씩 입력해서 실행​

![image](https://github.com/ragu6963/TIL/assets/32388270/bd3af0bb-98a8-4b96-876c-400b6db84563)

2. 확장자가 .py인 파일에 작성된 파이썬 프로그램을 실행

![image](https://github.com/ragu6963/TIL/assets/32388270/6cfdbd58-6edc-4103-8364-486bd1f7b59e)

### 표현식과 값
#### 표현식(Expression)
-  값으로 평가될 수 있는 코드 조각

#### 값(Value)
- 표현식이 평가된 결과

#### 예시

    3 + 5

    표현식 : 3 + 5
    값 : 8

#### 평가
- 표현식을 실행하여 값을 얻는 과정

> 표현식을 순차적으로 평가하여 프로그램의 동작을 결정

#### 문장(statement)
- 실행 가능한 동작을 기술하는 코드 (조건문, 반복문, 함수 정의 등)

#### 표현식과 문장
> 문장은 보통 여러 개의 표현식을 포함

![image](https://github.com/ragu6963/TIL/assets/32388270/39aa9d7f-aa5b-44eb-a661-dae74c4af7b2)

## 타입
### 타입(Type)
- 변수나 값이 가질 수 있는 데이터의 종류를 의미
- 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지를 정의
- 타입은 2가지 요소로 이루어짐 
    - <span style='color:red'>“값”</span>과 <span style='color:red'>“값에 적용할 수 있는 연산”</span>

![image](https://github.com/ragu6963/TIL/assets/32388270/8124c2d4-f2b7-4c29-b11f-b08fb478b5d8)

### 데이터 타입
#### - Numeric Types
    int (정수), float (실수), complex (복소수)
#### - Sequence Types
    - list, tuple, range
#### - Text Sequence Type
    - str (문자열)
#### - Non-sequence Types
    - set, dict
#### - 기타
    - None, Boolean, Functions

#### 데이터 타입의 중요성
- 데이터 타입에 맞는 연산을 수행할 수 있기 때문

#### 산술 연산자
| 기호 | 연산자        |
|:---:|:----------:|
| -  | 음수 부호      |
| +  | 덧셈         |
| -  | 뺄셈         |
| *  | 곱셈         |
| /  | 나눗셈        |
| // | 정수 나눗셈 (몫) |
| %  | 나머지        |
| ** | 지수 (거듭제곱)  |

#### 연산자 우선순위
| 우선순위 | 연산자         | 연산                   |
|:----:|:-----------:|:--------------------:|
| 높음   | **          | 지수                   |
|      | -           | 음수 부호                |
|      | *, /, //, % | 곱셈, 나눗셈, 정수 나눗셈, 나머지 |
| 낮음   | +, -        | 덧셈, 뺄셈               |

#### 연산자 우선순위 예시

```python
# -16  (지수 먼저 계산됨)
-2 ** 4

# -16
-(2 ** 4)

# 16
(-2) ** 4
```

### 변수와 메모리 "값이 저장되는 법"

#### 변수(variable)
- 값을 저장하기 위한 이름

#### 변수 할당
- 표현식을 통해 변수에 값을 저장

#### 할당문
```python
degrees == 36.5 # (x) 수학에서 같다는 의미로 사용됨
```
- “변수 degrees는 값 36.5이다”
-> 프로그래밍에서는 아래와 같이 '할당' 사용

```python
degrees = 36.5
```
- “변수 degrees에 값 36.5를 <span style='color:red'>할당</span>했다”

```python
degrees = 'abc'
```

- "변수 degrees에 값 'abc'를 재할당했다."

#### 변수명 규칙
- 영문 알파벳, 언더스코어(_), 숫자로 구성
- 숫자로 시작할 수 없음
- 대소문자를 구분
- 아래 키워드는 파이썬의 내부 예약어로 사용할 수 없음

    ```python
    ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 
    'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
    'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
    'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    ```

#### 변수, 값 그리고 메모리
- 거리에 집 주소가 있듯이 메모리의 모든 위치에는 그 위치를 고유하게 식별하는 메모리 주소가 존재

![image](https://github.com/ragu6963/TIL/assets/32388270/52e0c752-978c-4b5c-b7a2-5cc88b4b3494)

- 객체 (Object)
    - 타입을 갖는 메모리 주소 내 값
    - “값이 들어있는 상자”
    
![image](https://github.com/ragu6963/TIL/assets/32388270/a0d8f9be-d895-4d93-b8ee-bbc9338ba1c5)


- 변수는 그 변수가 참조하는 객체의 메모리 주소를 가짐
- 변수 degrees는 값 36.5를 참조

![image](https://github.com/ragu6963/TIL/assets/32388270/b5dfec1e-9f57-4dba-bf47-d333c988a1ab)

#### 할당문
![image](https://github.com/ragu6963/TIL/assets/32388270/21737370-e926-4b74-9055-436ed9e26270)
1. 할당 연산자(=) 오른쪽에 있는 표현식을 평가해서 값(메모리 주소)을 생성
2. 값의 메모리 주소를 ‘=‘ 왼쪽에 있는 변수에 저장
    - 존재하지 않는 변수라면
        - 새 변수를 생성
    - 기존에 존재했던 변수라면
        - 기존 변수를 재사용해서 변수에 들어 있는 메모리 주소를 변경

#### 변수에 재할당
- 변수 double의 값은 무엇일까?

    ```python 
    number = 10
    double = 2 * number
    print(double)  # 20
    number = 5
    print(double)  # ??
    ```

- 변수 double에는 값 20의 주소가 들어 있으니 여전히 20을 참조

    ```python
    number = 10
    double = 2 * number
    print(double)  # 20
    number = 5
    print(double)  # 20
    ```
![image](https://github.com/ragu6963/TIL/assets/32388270/b1095d47-ba4b-4994-aff2-f70d63d844b6)


## 참고
### Style Guide
- 코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장 사항들의 모음

#### 파이썬 Style Guide
- 변수명은 무엇을 위한 변수인지 직관적인 이름을 가져야 함
- 공백(spaces) 4칸을 사용하여 코드 블록을 들여쓰기
- 한 줄의 길이는 79자로 제한하며, 길어질 경우 줄 바꿈을 사용
- 문자와 밑줄(_)을 사용하여 함수, 변수, 속성의 이름을 작성
- 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄을 추가

> 파이썬 스타일 가이드 PEP 8 참고 문서 : https://peps.python.org/pep-0008/

### Python Tutor

#### Python Tutor
- 파이썬 프로그램이 어떻게 실행되는지 도와주는 시각화 도우미
> https://pythontutor.com/

### 주석
#### 주석(comment)
- 프로그램 코드 내에 작성되는 설명이나 메모
- 인터프리터에 의해 실행되지 않음

    ```python
    # 이것은
    age = 10

    # 주석입니다
    print(age)

    """
    여러 줄 주석
    """
    ```

#### 주석의 목적
- 코드의 특정 부분을 설명하거나 임시로 코드를 비활성화할 때 
- 코드를 이해하거나 문서화하기 위해 
- 다른 개발자나 자신에게 코드의 의도나 동작을 설명하는 데 도움