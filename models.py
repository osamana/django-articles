from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from parler.models import TranslatedFields, TranslatableModel

from .managers import *
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .settings import *
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from programs.models import Show

'''
    news article
'''
#
#
# class NewsImage(models.Model):
#     # call like this: news_image_list = NewsArticle.images.all()
#     article = models.ForeignKey('NewsArticle', related_name='images')
#
#     image_original = models.ImageField(
#         verbose_name='Photo', blank=True, null=True, upload_to='thumbs/news/'
#     )
#     image = ImageSpecField(source='image_original',
#                            processors=[ResizeToFill(600, 450)],
#                            format='PNG',
#                            options={'quality': 60})
#     label = models.CharField(max_length=255, blank=True, null=True)


class NewsArticle(TranslatableModel):
    class Meta:
        verbose_name=_("News Article")
        verbose_name_plural = _('News Articles')

    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    translations = TranslatedFields(
        title=models.CharField(
            max_length=255, verbose_name=_('News Title')
        ),
        content=RichTextField(blank=True, null=True, verbose_name=_('News Content')),
        # tag_line=models.CharField(
        #     max_length=255, verbose_name='Tag Line'
        # )
    )

    show = models.ForeignKey(Show, blank=True, null=True, verbose_name=_('Related Show (Optional)'))

    # todo check functionality of help_text attribute
    publish_date = models.DateField(verbose_name=_('Publish Date'), help_text='Enter publish date', null=True)

    raw_image = models.ImageField(
        verbose_name=_('News Image'), blank=True, null=True, upload_to='thumbs/news/'
    )
    # prcessed thumbnail
    image = ImageSpecField(source='raw_image',
                               processors=[ResizeToFill(NEWS_IMG_W, NEWS_IMG_H)],
                               format='PNG',
                               options={'quality': NEWS_IMG_Q})

    view_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

    # custom manager
    objects = NewsArticleManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:article-detail', kwargs={
            'pk': self.id
        })

#
# class Advertisement(TranslatableModel):
#     translations = TranslatedFields(
#         title=models.CharField(
#             max_length=255, verbose_name='Title'
#         ),
#         discription=RichTextField(blank=True, null=True),
#         # tag_line=models.CharField(
#         #     max_length=255, verbose_name='Tag Line'
#         # )
#     )
#
#     is_shown = models.BooleanField(
#         verbose_name="Show this Ad", null=False, blank=False,
#     )
#     ad_image = models.ImageField(
#         verbose_name='Ad Photo', blank=False, null=False, upload_to='ads/'
#     )
#
#     image = ImageSpecField(source='ad_image',
#                            processors=[ResizeToFill(AD_W, AD_H)],
#                            format='PNG',
#                            options={'quality': AD_IMG_Q})
#
#     sponsers = models.ManyToManyField(
#         'Sponser', verbose_name='Sponsers',
#         blank=True,
#     )
#     link = models.URLField(verbose_name='URL', blank=True, null=True)
#     link_label = models.CharField(verbose_name='URL visit button label', blank=True, null=True, default='Visit Link',
#                                   max_length=200)
#
#     # custom manager
#     objects = AdManager()
#
#     def __unicode__(self):
#         return self.title
#
#
# class Sponser(models.Model):
#     name = models.CharField(
#         max_length=255, verbose_name='name / title'
#     )
#     image = models.ImageField(
#         verbose_name='icon / logo', blank=False, null=False, upload_to='ads/'
#     )
#
#     logo = ImageSpecField(source='image',
#                           processors=[ResizeToFill(100, 100)],
#                           format='PNG',
#                           options={'quality': 60})
#
#     def __unicode__(self):
#         return self.name
#
#
# class Banner(models.Model):
#     objects = BannerManager()
#
#     link = models.URLField(
#         verbose_name='Link URL'
#     )
#     visible = models.BooleanField(
#         verbose_name='Visible'
#     )
#     image_banner = models.ImageField(
#         verbose_name='Image', blank=False, null=False, upload_to='banners/'
#     )
#
#     image = ImageSpecField(source='image_banner',
#                            processors=[ResizeToFill(320, 40)],
#                            format='PNG',
#                            options={'quality': 60})
#
#     def __unicode__(self):
#         return 'Banner' + str(self.id)
