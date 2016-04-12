from django.contrib import admin
from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    pass
