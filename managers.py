import datetime
from django.db import models
from parler.managers import TranslatableQuerySet, TranslatableManager

from .settings import *


class NewsArticleQueryset(TranslatableQuerySet):
    def all(self):
        return self.translated()

    def by_date(self):
        return self.translated().order_by('-publish_date')

    def by_views(self):
        return self.translated().order_by('-view_count')

    # passed publish date
    def published(self):
        return self.translated().filter(publish_date__lte=datetime.date.today())


class NewsArticleManager(TranslatableManager):
    def get_queryset(self):
        return NewsArticleQueryset(self.model, using=self._db)

        # INFO: can construct nested queries using these

    def by_date(self):
        return self.get_queryset().by_date()

    def by_views(self):
        return self.get_queryset().by_views()

    def published(self):
        return self.get_queryset().published()

    def latest_articles(self, limit):
        return self.published().by_date()[0:limit]

    def all_articles(self):
        return self.published().by_date()

    def general_articles(self):
        return self.all_articles().filter(show=None)

    def latest_article(self):
        return self.published().by_date().first()

    def latest_articles_except_first(self, limit):
        return self.published().by_date()[1:limit + 1]

    def latest_show_articles_except_first(self, show, limit):
        return self.all_articles().filter(show=show)[1:limit + 1]

    def latest_show_article(self, show):
        return self.all_articles().filter(show=show).first()



#
# # ############################################################
#
#
# class AdQueryset(TranslatableQuerySet):
#     def shown(self):
#         return self.filter(is_shown=True)
#
#
# class AdManager(models.Manager):
#     def get_queryset(self):
#         return AdQueryset(self.model, using=self._db)
#
#     # INFO: can construct nested queries using these
#
#     def shown(self):
#         return self.get_queryset().shown()
#
#
# # ############################################################
#
#
# class BannerQueryset(models.QuerySet):
#     def shown(self):
#         return self.filter(visible=True)
#
#
# class BannerManager(models.Manager):
#     def get_queryset(self):
#         return BannerQueryset(self.model, using=self._db)
#
#     # INFO: can construct nested queries using these
#
#     def shown(self):
#         return self.get_queryset().shown()
