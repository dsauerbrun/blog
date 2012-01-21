from django.shortcuts import render_to_response
from blog.models import Blog

def index(request):
	entries = Blog.objects.all()
	return render_to_response('index.html',locals())
