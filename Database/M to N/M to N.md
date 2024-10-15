# Many to many relationships

- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
> 양쪽 모두에서 N:1 관계를 가짐

## N:1의 한계

- 1번 환자가 두 의사 모두에게 진료를 받고자 한다면 환자 테이블에 1번 환자 데이터가 중복으로 입력될 수 밖에 없음 (example.1)

- 동시에 예약 남기려면..? -> 예약 테이블을 따로 만들자

## 중개 모델

1. 예약 모델 생성

  - 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 생성
  - 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

```py
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


# 외래키 삭제
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

2. 예약 데이터 생성

  - 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
  - 의사와 환자 생성 후 예약 만들기

```py
# 예약 데이터 생성
doctor1 = Doctor.objects.create(name='allie')
patient1 = Patient.objects.create(name='carol')

Reservation.objects.create(doctor=doctor1, patient=patient1)

# 예약 정보 조회 - 의사, 환자가 예약 모델을 통해 각각 본인의 진료 내역 확인
doctor1.reservation_set.all()
patient1.reservation_set.all()

# 추가 예약 생성 - 1번 의사에게 새로운 환자 예약 생성
patient2 = Patient.objects.create(name='duke')
Reservation.objects.create(doctor=doctor1, patient=patient2)
```

#### Django에서는 'ManyToManyField'로 중개모델을 자동으로 생성

### ManyToManyField

- ManyToManyField() : M:N 관계 설정 모델 필드

  ```py
  # 환자 모델에 ManyToManyField 작성
  # 의사 모델에 작성해도 상관 없으며 참조/역참조 관계만 잘 기억할 것

  class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


  class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
  ```

  - 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
  - 생성된 중개 테이블 hospitals_patient_doctors 확인

  ```py
  # 의사 1명과 환자 2명 생성
  doctor1 = Doctor.objects.create(name='allie')
  patient1 = Patient.objects.create(name='carol')
  patient2 = Patient.objects.create(name='duke')

  # 예약 생성 (환자가 예약)
  # patient1이 doctor1에게 예약
  patient1.doctors.add(doctor1)

  # patient1 - 자신이 예약한 의사목록 확인
  patient1.doctors.all()

  # doctor1 - 자신의 예약된 환자목록 확인
  doctor1.patient_set.all()

  # doctor1이 patient2을 예약
  doctor1.patient_set.add(patient2)

  doctor1.patient_set.all()
  patient2.doctors.all()
  patient1.doctors.all()

  # 예약 취소하기
  # 이전에는 Reservation을 찾아서 지워야 했다면, 이제는 remove()로 삭제 가능

  # doctor1이 patient1 진료 예약 취소
  doctor1.patient_set.remove(patient1)
  doctor1.patient_set.all()
  patient1.doctors.all()

  # patient2가 doctor1 진료 예약 취소
  patient2.patient_set.remove(doctor1)
  patient2.doctors.all()
  doctor1.patient_set.all()
  ```

#### 만약 예약 정보에 병의 증상, 예약일 등 추가 정보가 포함되어야 한다면?

### 'through' argument

- 중개 테이블에 '추가 데이터'를 사용해 M:N 관계를 형성하려는 경우에 사용

  ```py
  # Reservation Class 재작성 및 through 설정
  # 이제는 예약 정보에 '증상'과 '예약일'이라는 추가 데이터가 생김
  class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


  class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


  class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
  ```

  - 데이터베이스 초기화 후 Migration 진행 및 shell_plus 진행

  ```py
  # 의사 1명과 환자 2명 생성
  doctor1 = Doctor.objects.create(name='allie')
  patient1 = Patient.objects.create(name='carol')
  patient2 = Patient.objects.create(name='duke')

  # 1. Reservation class를 통한 예약 생성
  reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
  reservation1.save()
  doctor1.patient_set.all()
  patient1.doctors.all()

  # 2. Patient 객체를 통한 예약 생성
  patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
  doctor1.patient_set.all()
  patient2.doctors.all()

  # 생성과 마찬가지로 의사와 환자 모두 각각 예약 삭제 가능
  doctor1.patient_set.remove(patient1)
  patient2.doctors.remove(doctor1)
  ```

### M:N 관계 주요 사항

- M:N 관계로 맺어진 두 테이블에는 물리적인 변화가 없음
- ManyToManyField는 중개 테이블을 자동으로 생성
- ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
  - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

- N:1 은 완전한 종속의 관계였지만 M:N은 종속적인 관계가 아니며 '의사에게 진찰받는 환자 & 환자를 진찰하는 의사' 이렇게 2가지 형태 모두 표현 가능

### ManyToManyField

- ManyToManyField(to, **options) : M:N 관계 설정 시 사용하는 모델 필드

- 양방향 관계
  - 어느 모델에서든 관련 객체에 접근할 수 있음

- 중복 방지 
  - 동일한 관계는 한번만 저장됨

#### 대표 인자 3가지

1. related_name
2. symmetrical
3. through

#### 1. 'related_name' arguments

- 역참조시 사용하는 manager name을 변경

![alt text](images/image-01.png)

```py
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    # ManyToManyField - related_name 작성
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()

# 변경 전 
doctor.patient_set.all()

# 변경 후 (변경 후 이전 manager name은 사용 불가)
doctor.patients.all()
```

#### 2. 'symmetrical' arguments

- 관계 설정 시 대칭 유무 설정
- ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
- 기본 값 : True
- ex. 팔로우, 맞팔로우 기능

```py
class Person(models.Model):
  # 대칭 기능 켜놓고 싶으면 기본 세팅
  friends = models.ManyToManyField('self')
  # 대칭 기능 끄고 싶으면 False로 세팅
  # friends = models.ManyToManyField('self', symmetrical=False)
```

- True일 경우
  - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함 (대칭)
  - 즉, 내가 당신의 친구라면 자동으로 당신도 내 친구가 됨

- False일 경우
  - True와 반대 (대칭되지 않음)

> source 모델 : 관계를 시작하는 모델
> target 모델 : 관계의 대상이 되는 모델

#### 3. 'through' arguments

- 사용하고자 하는 중개모델을 지정
- 일반적으로 "추가 데이터를 M:N 관계와 연결하려는 경우"에 활용

```py
class Patient(modes.Model):
  doctors = models.ManyToManyField(Doctor, through='Reservation')

class Reservation(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  symptom = models.TextField()
  reserved_at = models.DateTimeField(auto_now_add=True)
```

#### M:N 에서의 대표조작 methods

- add()
  - 관계 추가
  - '지정된 객체를 관련 객체 집합에 추가'

- remove()
  - 관계 제거
  - 관련 객체 집합에서 지정된 모델 객체를 제거


## 좋아요 기능 구현

### 모델 관계 설정

- Article(M) - User(N)
  - 0개 이상의 게시글은 0명 이상의 회원과 관련

> 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있음

1. Article 클래스에 ManyToManyField 작성

- Article - User (N:1)
  - N:1에서의 역참조
  - user.article_set

- Article - User (N:M)
  - N:1에서의 역참조
  - 유저가 좋아요 누른 모든 게시글
  - user.like_articles

```py
class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- related_name 지정안해주면 역참조 매니저 충돌남..

- like_users 필드 생성 시 자동으로 역참조 매니저 .article_set 가 생성됨
- 그러나 이전 N:1 (Article-User) 관계에서 이미 같은 이름의 매니저를 사용중
  - user.article_set.all() -> 해당 유저가 작성한 모든 게시글 조회

- user가 작성한 글 (user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 됨

> user와 관계된 ForeignKey 혹은 ManyToManyField 둘 중 하나에 related_name 작성 필요

#### User-Article간 사용 가능한 전체 related manager

- article.user
  - 게시글을 작성한 유저 - N:1

- user.article_set
  - 유저가 작성한 게시글(역참조) - N:1

- article.like_users
  - 게시글을 좋아요 한 유저 - M:N

- user.like_articles
  - 유저가 좋아요 한 게시글(역참조) - M:N

### 기능 구현

1. url 작성

```py
# articles/urls.py

path('<int:article_pk>/likes/', views.likes, name='likes'),
```

2. view 함수 작성
```py
def likes(request, article_pk):
    # 어떤 글에 좋아요를 눌렀는지 글을 먼저 조회
    article = Article.objects.get(pk=article_pk)

    # 좋아요를 추가하는 것이냐 / 취소하는 것이냐
    # 만약 좋아요를 요청한 유저가 해당 글의 좋아요를 누른 유저 목록에 포함되어있다면(좋아요 취소)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    # 그게 아니라 좋아요를 요청한 유저가 해당글의 좋아요를 누른 유저 목록에 없다면(좋아요 추가)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```

3. index 템플릿에서 각 게시글에 좋아요 버튼 출력

```html
  <form action="{% url "articles:likes" article.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
      <input type="submit" value="좋아요 취소">
    {% else %}
      <input type="submit" value="좋아요">
    {% endif %}
  </form>
```

## 팔로우 기능 구현
### 프로필 페이지

- 각 회원의 개인 프로필 페이지에 팔로우 기능을 구현하기 위해 프로필 페이지를 먼저 구현하기

#### 프로필 구현

1. url 작성
```py
# accounts/urls.py

path('profile/<username>/', views.profile, name='profile'),
# path('profile/<str:username>/', views.profile, name='profile'),
```

2. view 함수 작성
```py
# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
    # 어떤 유저의 프로필을 보여줄건지 유저를 조회(username을 사용해서 조회)
    User = get_user_model()
    person = User.objects.get(username=username)
    # person = get_user_model().objects.get(username=username)
    context={
        'person':person,
    }
    return render(request, 'accounts/profile.html', context)
```

3. profile 템플릿 작성
```html
<!-- accounts/profile.html -->

<h1>{{ person.username }}의 프로필</h1>

{% comment %} 유저가 작성한 게시글 {% endcomment %}
<h2>{{ person.username }} 작성한 게시글</h2>
{% for article in person.article_set.all %}
  <p>{{ article.title }}</p>
{% endfor %}

{% comment %} 유저가 작성한 댓글 {% endcomment %}
<h2>{{ person.username }} 작성한 댓글</h2>
{% for comment in person.comment_set.all %}
  <p>{{ comment.content }}</p>
{% endfor %}

{% comment %} 유저가 좋아요한 게시글 {% endcomment %}
<h2>{{ person.username }} 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}
```

4. 프로필 페이지로 이동할 수 있는 링크 작성

```html
<!-- articles/index.html -->
{% for article in articles %}
  <a href="{% url "accounts:profile" user.username %}">내 프로필</a>
```

### 모델 관계 설정

- User(M) - User(N) : 0명 이상의 회원은 0명 이상의 회원과 관련
> 회원은 0명 이상의 팔로워를 가질 수 있고, 0명 이상의 다른 회원들을 팔로잉 할 수 있음

- ManyToManyField 작성
  ```py
  # accounts/models.py

  class User(AbstractUser):
      followings = models.ManyToManyField("self", symmetrical=False, related_name='followers')
  ```
- 참조 
  - 내가 팔로우하는 사람들 (팔로인, followings)

- 역참조
  - 상대방 입장에서 나는 팔로워 중 한 명 (팔로워, followers)

> 바뀌어도 상관 없으나 관계 조회시 생각하기 편한 방향으로 정한것

![alt text](images/image-02.png)

### 기능 구현

1. url 작성

```py
# accounts/urls.py

path('<int:user_pk>/follow', views.follow, name='follow'),
```
2. view 함수 작성

```py
def follow(request, user_pk):
    User = get_user_model()
    # 팔로우 요청을 보내는 대상
    you = User.objects.get(pk=user_pk)
    # 나 (팔로우 요청하는 사람)
    me = request.user

    # 나와 팔로우 대상자가 같지 않은 경우만 진행
    if me != you:
        # 만약 내가 상대방의 팔로워 목록에 이미 있다면 팔로우 취소
        if me in you.followers.all():
            you.followers.remove(me)
            # 위와 아래는 같은 것 삭제함. 방향성의 문제일 뿐
            # me.followings.remove(you)
        else:
            you.followers.add(me)
            # me.followings.add(you)
    return redirect('accounts:profile', you.username)
```

3. 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성

```html
<div>
  팔로잉: {{ person.followings.all|length}} / 팔로워 : {{ person.followers.all|length }}
</div>
{% if request.user != person %}
  <div>
    <form action="{% url "accounts:follow" person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="Unfollow">
      {% else %}
        <input type="submit" value="Follow">
      {% endif %}
    </form>
  </div>
{% endif %}
```

## Fixtures

- django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
> 데이터는 데이터베이스 구조에 맞추어 작성 되어있음

- django에서는 fixtures를 사용해 앱에 초기 데이터 제공

- dumpdata : 생성(데이터 추출)
- loaddata : 로드(데이터 입력)

### dumpdata

- 데이터베이스의 모든 데이터를 추출

```bash
python manage.py dumpdata --indent 4 articles.article > articles.json
python manage.py dumpdata --indent 4 articles.comment > comments.json
python manage.py dumpdata --indent 4 accounts.user > users.json
```

### loaddata

- fixtures 데이터를 데이터베이스로 불러오기

- fixtures 파일 기본 경로
  - app_name/fixtures/

> django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾아 load

![alt text](images/image-03.png)

```bash
python manage.py loaddata articles.json users.json comments.json
```

#### loaddata 순서 주의사항

- loaddata를 한번에 실행하지 않고 별도로 실행한다면 모델관계에 따라 load 순서가 중요할 수 있음..(key 이리저리 얽혀있음)

- user -> article -> comment 순으로 data를 load 해야 오류가 발생하지 않음


## Improve query

- query 개선하기
> 같은 결과를 얻기 위해 DB 측에 보내는 query 개수를 점차 줄여 조회하기

### 사전 준비

- fixtures 데이터
  - 게시글 10개 / 댓글 100개 / 유저 5개

```bash
python manage.py migrate
python manage.py loaddata users.json articles.json comments.json
```

### annotate

- SQL의 GROUP BY를 사용
- 쿼리셋의 각 객체에 계산된 필드를 추가
- 집계 함수(count, sum 등)와 함께 자주 사용됨

#### annotate 예시

```py
Book.objects.annotate(num_authors=Count('authors'))
```

- 의미
  - 결과 객체에 'num_authors'라는 새로운 필드를 추가
  - 이 필드는 각 책과 연관된 저자의 수를 계산

- 결과
  - 결과에는 기존 필드와 함께 'num_authors' 필드를 가지게 됨
  - book.num_authors로 해당 책의 저자 수에 접근할 수 있게 됨

```py
articles = Article.objects.annotate(Count('comment')).order_by('-pk')
```
```html
<p>댓글개수 : {{ article.comment__count }}</p>
```

### select_related

- SQL의 INNER JOIN을 사용

- 1:1 또는 N:1 참조 관계에서 사용
  - ForeignKey나 OneToOneField 관계에 대해 JOIN을 수행
- 단일 쿼리로 관련 객체를 함께 가져와 성능을 향상

#### select_related 예시

```py
Book.objects.select_related('publisher')
```

- 의미
  - Book 모델과 연관된 Publisher 모델의 데이터를 함께 가져옴
  - ForeignKey 관계인 'publisher'를 JOIN 하여 단일 쿼리 만으로 데이터를 조회

- 결과 
  - Book 객체를 조회할 때 연관된 Publisher 정보도 함께 로드
  - book.publisher.name 과 같은 접근이 추가적인 데이터베이스 쿼리 없이 가능

```py
# 게시글 조회하면서 작성자 같이 조회

articles = Article.objects.select_related('user').order_by('-pk')
```

### prefetch_related

- SQL이 아닌 Python을 사용한 JOIN을 진행
  - 관련 객체들을 미리 가져와 메모리에 저장하여 성능을 향상

- M:N 또는 N:1 역참조 관계에서 사용
  - ManyToManyField나 역참조 관계에 대해 별도의 쿼리를 실행

#### prefetch_related 예시

```py
Book.objects.prefetch_related('authors')
```
- 의미
  - Book과 Author는 ManyToMany 관계로 가정
  - Book 모델과 연관된 모든 Author 모델의 데이터를 미리 가져옴
  - Django가 별도의 쿼리로 Author 데이터를 가져와 관계를 설정

- 결과
  - Book 객체들을 조회한 후, 연관된 모든 Author 정보가 미리 로드됨
  - for author in book.authors.all() 와 같은 반복이 추가적인 데이터베이스 쿼리 없이 실행됨

```py
# 게시글을 조회하면서 참조된 댓글까지 한번에 조회

articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
```
### select_related & prefetch_related

```py
# 게시글 + 각 게시글의 댓글 목록 + 댓글의 작성자를 한번에 조회

articles = Article.objects.prefetch_related(
    Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
).order_by('-pk')
```

## 참고 
### 'exists' method

- QuerySet에 결과가 하나 이상 존재하는지 여부를 확인하는 메서드
- 결과가 포함되어 있으면 True를 반환하고, 결과가 포함되어 있지 않으면 False를 반환

- 데이터베이스에 최소한 쿼리만 실행하여 효율적
- 전체 QuerySet을 평가하지 않고 결과의 존재 여부만 확인
> 대량의 QuerySet에 있는 특정 객체 검색에 유용

```py
if request.user in article.like_users.all():
# 위 아래 동일하게 사용 가능
if article.like_users.filter(pk=request.user.pk).exists():
```

### 한꺼번에 dump하기
### loaddata 인코딩 에러

1. dumpdata시 추가 옵션 작성

```bash
python -Xutf8 manage.py dumpdata [데이터 이름]
```

2. 메모장 활용

  1) 메모장으로 json 열기
  2) 다른 이름으로 저장 클릭
  3) 인코딩을 UTF8 선택 후 저장
