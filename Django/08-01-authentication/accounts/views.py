from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        # 로그인 로직 작성
        # ModelForm이 아니라, Form 이기 때문에 request 먼저 작성해줘야함
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 만약 인증된 사용자라면 로그인 진행(세션 데이터 생성)
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')