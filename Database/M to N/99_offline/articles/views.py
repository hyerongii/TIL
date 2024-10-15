from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    context = {
        'article' : article,
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form
    }
    return render(request, 'articles/update.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail', article_pk)

def comment_delete(request, article_pk):
    comment = Comment.objects.get(pk=article_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
