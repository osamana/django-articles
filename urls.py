from django.conf.urls import url

from .views import NewsArticleDetail, NewsArticleList

urlpatterns = [
    url(r'article/(?P<pk>\d+)$', NewsArticleDetail.as_view(), name='article-detail'),
    url(r'$', NewsArticleList.as_view(), name='article-list'),
]