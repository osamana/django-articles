from __future__ import unicode_literals
from watson import search as watson
from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        news_article = self.get_model("NewsArticle")
        watson.register(news_article)
