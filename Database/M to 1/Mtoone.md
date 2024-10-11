# Many to one relationships
## 모델 관계

한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

### Comment(N) - Article(1)
0개 이상의 댓글은 1개의 게시글에 작성될 수 있다.

- 테이블 관계
  ![alt text](images/image-01.png)

## 댓글 모델 정의

- ForeignKey 클래스의 인스턴스 이름은 **참조하는 모델 클래스 이름의 단수형**으로 작성하는 것을 권장
- 외래 키는 ForeignKey 클래스를 작성하는 위치와 관계없이 테이블의 마지막 필드로 생성됨

```py
class Comment(models.Model):
    # ForeignKey(상대 모델 클래스, 상대모델클래스가 삭제되었을때 댓글을 어떻게 처리할지)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
### ForeignKey(to, on_delete)

- 한 모델이 다른 모델을 참조하는 관계를 설정하는 필드

> N:1 관계 구현
> 데이터베이스에서 외래 키로 구현

- to
  - 참조하는 모델 class 이름

- on_delete
  - 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래키를 가진 객체(N)를 어떻게 처리할 지 정의하는 설정(데이터 무결성)

#### on_delete의 'CASCADE'

- 참조 된 객체(부모 객체)가 삭제될 때 이를 참조하는 모든 객체도 삭제되도록 지정

> 기타 on_delete 설정 값 참고

### 모델 생성 후 makemigrations -> migrate!!

- 댓글 테이블의 article_id 외래 키 필드 확인
- 만들어지는 필드 이름
  - '참조 대상 클래스 이름' + _ + 'id'
  ![alt text](images/image-02.png)

> 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장되었던 이유

## 댓글 생성 연습

1. shell_plus 실행 및 게시글 작성

```bash
# shell plus 실행
python manage.py shell_plus

# 게시글 생성
Article.objects.create(title='title', content='content')
```

2. 댓글 생성

```bash
# Comment 클래스의 인스턴스 comment 생성
comment = Comment()

# 인스턴스 변수 저장
comment.content = 'first comment'

# 게시글 조회
article = Article.objects.get(pk=1)

# 외래 키 데이터 입력
comment.article = article
# 또는 comment.article_id = article.pk 표현으로 
# pk 값을 직접 외래 키 컬럼에 넣어 줄수도 있지만 권장하지 않음

# 댓글 저장 및 확인
comment.save()
```

3. comment 인스턴스를 통한 article 값 참조하기

```bash
comment.pk
=> 1

comment.content
=> 'first comment'

comment.article
=> <Article: Article object (1)>

comment.article_id 
=> 1

# 1번 댓글이 작성된 게시물의 pk 조회
comment.article.pk
=> 1

# 1번 댓글이 작성된 게시물의 content 조회
comment.article.content
=> 'content'
```

4. 두번째 댓글 생성
```bash
comment = Comment(content = 'second comment', article=article)
comment.save()
```

# 관계 모델 참조
## 역참조

- N:1 관계에서 1에서 N을 참조하거나 조회하는 것 (1 -> N)

- 모델 간의 관계에서 관계를 정의한 모델이 아닌, 관계의 대상이 되는 모델에서 연결된 객체들에 접근하는 방식

> N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만, 1은 N에 대한 참조방법이 존재하지 않아 별도의 역참조 키워드가 필요

### 역참조 사용 예시

![alt text](images/image-03.png)
![alt text](images/image-04.png)

#### related manager

- N:1 혹은 M:N 관계에서 역참조 시에 사용하는 매니저
> 'objects' 매니저를 통해 QuerySet API를 사용했던 것처럼 related manager를 통해 QuerySet API를 사용할 수 있게 됨

- N:1 관계에서 생성되는 Related manager의 이름은 "모델명_set" 형태로 자동 생성됨
  - 관계를 직접 정의하지 않은 모델에서 연결된 객체들을 조회할 수 있게함

- 특정 댓글의 게시글 참조(Comment -> Article)
  - comment.article

- 특정 게시글의 댓글 목록 참조 (Article -> Comment)
  - article.comment_set.all()

```bash
#1번 게시글에 작성된 모든 댓글 조회하기 (역참조)
>>> article.comment_set.all()
<QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>
```

# 댓글 구현
## 댓글 CREATE

1. 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 정의
```py
# articles/forms.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('content',)

2. detail view 함수에서 CommentForm을 사용하여 detail 페이지에 렌더링

  - 외래 키 필드 데이터는 사용자로 부터 입력 받는 값이 아닌 view 함수 내에서 다른 방법으로 전달 받아 저장되어야함

```py
# articles/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)
```
```html
  <form action="#" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```
3. url 작성 및 action 값 작성

  - 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까?
  - detail 페이지의 URL을 살펴보면
  path('<int:pk>/', views.detail, name='detail')
  에서 해당 게시글의 pk 값이 사용되고 있음

  - 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값
```py
# articles/urls.py

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```
```html
{% comment %} 댓글 작성 {% endcomment %}
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit">
</form>
```

4. comments_create view 함수 정의

> url로 받은 pk 인자를 게시글을 조회하는데 사용

- save(commit=False)
  - DB에 저장 요청을 보내지 않고 인스턴스만 반환

```py
# articles/views.py
def comments_create(request, pk):
    # 어떤 게시글에 작성되는지 게시글을 조회
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
        # 외래 키 데이터를 넣는 타이밍이 필요
        # 외래 키를 넣으려면 2가지 조건이 필요
        # 1. comment 인스턴스 필요
        # 2. save 메서드가 호출 되기 전이어야 함
        # 그런데 comment 인스턴스는 save 메서드가 호출되어야 생성됨
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

## 댓글 READ

1. detail view 함수에서 전체 댓글 데이터를 조회

```py
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해당 게시글에 작성된 모든 댓글 조회 (역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)
```
2. 전체 댓글 출력 및 확인

```html
  {% comment %} 댓글 출력 {% endcomment %}
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
      </li>
    {% endfor %}
  </ul>
```
## 댓글 DELETE

1. 댓글 삭제 url 작성

```py
# articles/urls.py

path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
```

2. 댓글 삭제 view 함수 정의
```py
def comments_delete(request, article_pk, comment_pk):
    # 어떤 댓글 삭제할지 조회
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

3. 댓글 삭제 버튼 작성
```html
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="#" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      </li>
    {% endfor %}
  </ul>
```

# 참고
## 데이터 무결성

- 데이터베이스에 저장된 데이터의 정확성, 일관성, 유효성을 유지하는 것
- 데이터베이스에 저장된 데이터 값의 정확성을 보장하는 것

> 중요성
  1. 데이터의 신뢰성 학보
  2. 시스템 안정성
  3. 보안 강화

## admin site 댓글 등록

- Comment 모델을 admin site에 등록해 CRUD 동작 확인하기

```py
# articles/admin.py
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```

## 댓글 추가 구현

1. 댓글이 없는 경우 대체 콘텐츠 출력
  - for empty 태그 사용하기

2. 댓글 개수 출력하기
  - DTL filter - 'length' 사용

  ```py
  {{ comments|length }}
  {{ article.comment_set.all|length }}
  ```

  - QuerySet API - 'count()' 사용

  ```py
  {{ article.comment_set.count }}
  ```