from django.contrib import admin
from blog.models import Blog
from blog.models import Image
from blog.models import Comment


class AdminBlog(admin.ModelAdmin):
	pass

admin.site.register(Blog, AdminBlog)
admin.site.register(Image, AdminBlog)
admin.site.register(Comment, AdminBlog)
