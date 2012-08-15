from django.contrib import admin
from django import forms
from django.forms import ModelForm
from posting.models import Blog
from posting.models import Image
from posting.models import Comment
from moneytracker.models import Expense
from moneytracker.models import Month
from moneytracker.models import Category
from moneytracker.models import PayMethod

class AdminBlog(admin.ModelAdmin):
	list_display = ('title','date','text','isPrivate')
	list_filter = ('title','date','text','isPrivate')
	search_fields = ('title','date','text','isPrivate')

#class testing(ModelForm):
#	monthform = forms.CharField(max_length=100)
#	def save(self,commit=False,force_insert=False,force_update=False):
#		commit=False
#		m = super(testing, self).save(commit=commit,month=self.cleaned_data['monthform'])
#	class Meta:
#		model= Expense
#
class AdminExpense(admin.ModelAdmin):
	list_display = ('title','date','has_category','has_payMethod','amount','recurring')
	list_filter = ('title','date','has_category','has_payMethod','amount','recurring')
	search_fields = ('title','date','has_category','has_payMethod','amount','recurring')
	

class generic(admin.ModelAdmin):
	pass

admin.site.register(Blog, AdminBlog)
admin.site.register(Image, generic)
admin.site.register(Comment, generic)
admin.site.register(Expense, AdminExpense)
admin.site.register(Month, generic)
admin.site.register(Category, generic)
admin.site.register(PayMethod, generic)
