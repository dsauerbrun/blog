from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from blog.models import Blog
from blog.models import Image

def index(request):
	if request.user.is_staff:
		entries = Blog.objects.all()
	else:
		entries = Blog.objects.filter(isPrivate=False)
	images = Image.objects.all()
	return render_to_response('index.html',locals(),RequestContext(request))

