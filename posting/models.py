from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib import admin

class Blog(models.Model):
	title = models.CharField(max_length=32)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	isPrivate= models.BooleanField(default=False)
	def displayText(self):
		return mark_safe(self.text)
	def __unicode__(self):
		return u'%s' % ( self.title)	
class Comment(models.Model):
	text = models.TextField(null=False)
	date = models.DateTimeField(auto_now_add=True)
	user = models.CharField(max_length=20)
	belongs_to_blog = models.ForeignKey('Blog')

class Image(models.Model):
	image_thumb = ImageWithThumbsField(upload_to='uploads',sizes=((150,150),))
	belongs_to_blog = models.ForeignKey('Blog')
	title = models.CharField(max_length=32)
	def __unicode__(self):
		return u'%s' % ( self.title)	

class Location(models.Model):
	title = models.CharField(max_length=20)
	latitude = models.DecimalField(max_digits=11,decimal_places=6,null=False)
	longitude = models.DecimalField(max_digits=11,decimal_places=6,null=False)
	date = models.DateTimeField(auto_now_add=True)
	note = models.TextField(null=True) 
