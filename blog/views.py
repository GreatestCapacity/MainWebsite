from django.http import Http404
from django.shortcuts import render
from blog.models import Article, Content

# Create your views here.


def index(request):
    try:
        latest_article_list = Article.objects.order_by('-pubtime')[:5]
    except Article.DoesNoExist:
        raise Http404('No')
    context = {'latest_article_list': latest_article_list}
    return render(request, 'index.html', context)


def article(request, article_id, content_id):
    artc = Article.objects.get(pk=article_id)
    if content_id == 'latest':
        contnt = artc.content_set.order_by('-sbmt_time')[0]
    else:
        contnt = artc.content_set.get(pk=content_id)
    return render(request, 'article.html', {'article': artc, 'content': contnt})
