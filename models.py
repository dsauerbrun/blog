from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
	title = models.CharField(max_length=32)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	isPrivate= models.BooleanField(default=False)
	def __unicode__(self):
		return u'%s' % ( self.title)	
class Image(models.Model):
	image_field = models.ImageField(upload_to='uploads/')
	belongs_to_blog = models.ForeignKey('Blog')
	title = models.CharField(max_length=32)
	def __unicode__(self):
		return u'%s' % ( self.title)	

