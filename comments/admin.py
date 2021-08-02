from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Articles, CommentsMptt


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_published')


admin.site.register(CommentsMptt, MPTTModelAdmin)
