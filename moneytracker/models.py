from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib import admin
import datetime
import operator


class Category(models.Model):
	title= models.CharField(max_length=32)
	def __unicode__(self):
		return u'%s' % ( self.title)	
	class Meta:
		ordering= ['title']

class PayMethod(models.Model):
	title= models.CharField(max_length=32)
	def __unicode__(self):
		return u'%s' % ( self.title)	
	class Meta:
		ordering= ['title']
"""
class Expense_Month(models.Model):
	month = models.ForeignKey('Month')
	expense = models.ForeignKey('Expense')
"""	

class Month(models.Model):
	#title = models.CharField(max_length=32)
	year = models.IntegerField(null=False)
	month = models.IntegerField(null=False)
	available = models.DecimalField(max_digits=9,decimal_places=2,null=False)
	def save(self,*args,**kwargs):
		super(Month,self).save(*args,**kwargs)
		recurring=Expense.objects.filter(recurring=True)
		for e in recurring:
			e.month.add(self)
			e.save()
		
	def total(self):
		total = 0
		for e in self.expense_set.all():
			total += e.amount
		return total
	def __unicode__(self):
		return u'%s' % ( str(self.month)+"/"+str(self.year))	

class Expense(models.Model):
	def get_most_category():
		catList=Expense.objects.values_list('has_category',flat=True)
		categories={}
		for i in catList:
			if i in categories:
				categories[i]+=1
			else:
				categories[i]=1
		return Category.objects.get(pk=max(categories.iteritems(), key=operator.itemgetter(1))[0])	
	def get_last_month():
		month= Month.objects.order_by('-id')[:1]
		if not month:
			return null
		else:
			return month
	title = models.CharField(max_length=32)
	date = models.DateField(default=datetime.datetime.now)
	has_category = models.ForeignKey('Category', default=get_most_category)
	has_payMethod = models.ForeignKey('PayMethod')	
	note = models.TextField(blank=True,null=True)
	recurring = models.BooleanField(default=False)
	amount = models.DecimalField(max_digits=9,decimal_places=2,null=False)
	month=models.ManyToManyField('Month',default=get_last_month)
	def __unicode__(self):
		return u'%s' % ( self.title)	
	class Meta:
		ordering= ['date']
