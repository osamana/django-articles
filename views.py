from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView, ListView
from .models import NewsArticle
from programs.models import *
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


class NewsArticleDetail(DetailView, HitCountMixin):
    model = NewsArticle
    context_object_name = 'article'
    http_method_names = [u'get']
    template_name = 'news/detail/news.html'

    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(NewsArticleDetail, self).get_context_data(**kwargs)

        if self.object:
            hit_count = HitCount.objects.get_for_object(self.object)
            hits = hit_count.hits
            context['hitcount'] = {'pk': hit_count.pk}

            if self.count_hit:
                hit_count_response = self.hit_count(self.request, hit_count)
                if hit_count_response.hit_counted:
                    hits = hits + 1
                context['hitcount']['hit_counted'] = hit_count_response.hit_counted
                context['hitcount']['hit_message'] = hit_count_response.hit_message

            context['hitcount']['total_hits'] = hits

        return context


class NewsArticleList(ListView):
    context_object_name = 'article_list'
    http_method_names = [u'get']
    template_name = 'news/list/news.html'
    queryset = NewsArticle.objects.all_articles()
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(NewsArticleList, self).get_context_data(**kwargs)
        return context
