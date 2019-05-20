from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>', views.article, name='article')
]
