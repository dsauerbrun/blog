from django.contrib import admin
from posting.models import Blog
from posting.models import Image
from posting.models import Comment


class AdminBlog(admin.ModelAdmin):
	list_display = ('title','date','text','isPrivate')
	list_filter = ('title','date','text','isPrivate')
	search_fields = ('title','date','text','isPrivate')
class generic(admin.ModelAdmin):
	pass

admin.site.register(Blog, AdminBlog)
admin.site.register(Image, generic)
admin.site.register(Comment, generic)
