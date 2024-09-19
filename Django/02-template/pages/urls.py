from django.urls import path
# 명시적 상대경로
from . import views

# app 마다 urls.py 작성해서 따로따로 관리하기
app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index')
]
