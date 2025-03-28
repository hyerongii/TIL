from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # 단일 게시글 조회 (고유한 값만 가지고 옴)
    # article = Article.objects.get(id=pk) 
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    # 게시글 작성 페이지 응답
    return render(request, 'articles/new.html')

def create(request):
    # 1. 사용자 요청으로부터 입력 데이터를 추출
    # 2. 추출한 입력 데이터를 활용해 DB에 저장 요청
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 저장 1 - 인스턴스 활용
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 저장 2 => 2번 사용하는거 권장!!!!
    article = Article(title = title, content = content)
    article.save()

    # 저장 3 
    # Article.objects.create(title=title, content=content)

    # new 만들고 본 페이지 게시글들 있는 곳으로 이동시키려면
    # return redirect('articles:index')

    # new -> 만들고 그 게시글로 이동시키려면
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()

    # 메인페이지로 이동
    return redirect('articles:index')

def edit(request, pk):
    # 어떤 게시글 수정할지 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 어떤 게시글 수정할지 조회
    article = Article.objects.get(pk=pk)

    # 사용자로부터 받은 새로운 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 기존 게시글의 데이터를 사용자로 받은 데이터로 새로 할당
    article.title = title
    article.content = content

    # 저장
    article.save()
    
    return redirect('articles:detail', article.pk)