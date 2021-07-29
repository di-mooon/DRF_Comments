from django.contrib import admin
from .models import Articles, Comments
# Register your models here.


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','date','is_published')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','date','is_published')