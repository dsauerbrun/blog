from django.contrib import admin
from blog.models import Blog
from blog.models import Image
from blog.models import Comment


class AdminBlog(admin.ModelAdmin):
	list_display = ('title','date','text','isPrivate')
	list_filter = ('title','date','text','isPrivate')
	search_fields = ('title','date','text','isPrivate')
class generic(admin.ModelAdmin):
	pass

admin.site.register(Blog, AdminBlog)
admin.site.register(Image, generic)
admin.site.register(Comment, generic)
