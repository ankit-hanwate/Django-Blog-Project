from django.contrib import admin
from .models import Post, Category

class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content', 'date']

    class Meta:
        model = Post


admin.site.register(Post, AdminPost)
admin.site.register(Category)