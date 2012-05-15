from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from blog.models import Blog
from blog.models import Image
from blog.models import Comment
from django.forms import ModelForm

def index(request):
	if request.user.is_staff:
		entries = Blog.objects.all()
	else:
		entries = Blog.objects.filter(isPrivate=False)
	images = Image.objects.all()
	comments = Comment.objects.all()
	form = CommentForm()
	#return render_to_response('index.html',locals(),RequestContext(request))
	return render_to_response('starter-template.html',locals(),RequestContext(request))

class CommentForm(ModelForm):
	class Meta:
		model=Comment
		exclude =["blog"]

def add_comment(request, pk):
	p = request.POST
	
	if p.has_key("text") and p["text"]:
		author = "Anonymous"
		if p["user"]: author = p["user"]
		print pk
		comment = Comment(belongs_to_blog=Blog.objects.get(pk=pk))
		cf = CommentForm(p, instance=comment)
		cf.fields["user"].required = False

		#comment = cf.save(commit=False)
		comment.text = p["text"]
		comment.user = author
		comment.save()
	return HttpResponseRedirect(reverse("blog_index"))
