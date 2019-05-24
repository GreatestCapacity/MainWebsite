from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>', views.article, name='article'),
    path('article/<int:article_id>/<str:content_id>', views.article, name='article'),
]
