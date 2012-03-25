from django.contrib import admin
from blog.models import Blog
from blog.models import Image


class AdminBlog(admin.ModelAdmin):
	pass

admin.site.register(Blog, AdminBlog)
admin.site.register(Image, AdminBlog)
