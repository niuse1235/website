from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
#프로젝트에 application을 넣고 빼는 작업운 url을 연결하는 작업과같음

