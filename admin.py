from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms
from parler.admin import *


#
# class NewsAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#
#     class Meta:
#         model = NewsArticle
#         exclude = ['view_count', 'share_count']
#
# class NewsImageInline(admin.TabularInline):
#     model = NewsImage
#     extra = 3


class NewsAdmin(TranslatableAdmin):
    # form = NewsAdminForm
    fields = ['title', 'content', 'publish_date', 'raw_image', 'show']
    list_display = ['title', 'publish_date', 'view_count']
    list_display_links = ['title']
    list_editable = []
    list_filter = ['publish_date']
    search_fields = ['translations__title', 'translations__content']
    # exclude = ['view_count', 'share_count']
    # inlines = [NewsImageInline, ]

    class Meta:
        model = NewsArticle

#
# class AdAdmin(TranslatableAdmin):
#     list_display = ['title', ]
#     list_display_links = ['title']
#     search_fields = ['translations__title', 'translations__content']
#
#     class Meta:
#         model = Advertisement
#
#
# class SponserAdmin(admin.ModelAdmin):
#     list_display = ['name', ]
#     list_display_links = ['name']
#     search_fields = ['name']
#
#
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ['link', ]
#     list_display_links = ['link']
#
#     class Meta:
#         model = Banner


admin.site.register(NewsArticle, NewsAdmin)
# admin.site.register(Sponser, SponserAdmin)
# admin.site.register(Advertisement, AdAdmin)
# admin.site.register(Banner, BannerAdmin)
