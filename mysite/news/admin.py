from django.contrib import admin

# Register your models here.
from .models import Category, Article, Feed

from .define import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_homepage', 'layout', 'status', 'ordering')
    # prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_homepage', 'layout', 'status')
    search_fields = ('name',)

    class Media:
        js = ('my_admin/js/general.js', 'my_admin/js/slugify.min.js', 'my_admin/js/jquery-3.6.0.min.js')
        css = {
            'all': ('my_admin/css/custom.css',)
        }

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    # prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'special', 'publish_date')
    search_fields = ('name',)

    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    # prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status',)
    search_fields = ('name',)

    class Media:
        js = ADMIN_SRC_JS

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)

admin.site.site_header = "My Site Admin"