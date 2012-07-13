from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from blog.models import Blog
from blog.models import Image
from blog.models import Comment
from django.forms import ModelForm,Textarea
import os

def index(request):
	if request.user.is_staff:
		entries = Blog.objects.all()
	else:
		entries = Blog.objects.filter(isPrivate=False)
	entries.order_by('date')
	for entry in entries:
		entry.text=entry.text.replace('\n','<br />')	
	images = Image.objects.all()
	comments = Comment.objects.all()
	form = CommentForm()
	#return render_to_response('index.html',locals(),RequestContext(request))
	return render_to_response('starter-template.html',locals(),RequestContext(request))

class CommentForm(ModelForm):
	class Meta:
		model=Comment
		widgets = {
			'text': Textarea(attrs={'class':'span6 addCommentInput','resizable':'false'}),
			'user': Textarea(attrs={'class':'addCommentInput','resizable':'false'}),
		}
		exclude =["blog"]

def add_comment(request, pk):
	p = request.POST
	
	if p.has_key("text") and p["text"]:
		author = "Anonymous"
		if p["user"]: author = p["user"]
		comment = Comment(belongs_to_blog=Blog.objects.get(pk=pk))
		cf = CommentForm(p, instance=comment)
		cf.fields["user"].required = False

		#comment = cf.save(commit=False)
		comment.text = p["text"]
		comment.user = author
		comment.save()
	return HttpResponseRedirect(reverse("blog_index"))
#	else:
#		return HttpResponseRedirect(reverse("blog_index",args=[p["user"]]))
		
