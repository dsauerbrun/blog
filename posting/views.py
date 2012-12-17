from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from posting.models import Blog
from posting.models import Image
from posting.models import Comment
from posting.models import Location
from django.forms import ModelForm,Textarea,TextInput,SelectMultiple,MultipleChoiceField,CheckboxSelectMultiple
from posting.posting_forms import location_form
import os
import json
import navbarbuilder

def index(request):
	menu = navbarbuilder.get_navbar(request)	
	if request.user.is_staff:
		entries = Blog.objects.all()
	else:
		entries = Blog.objects.filter(isPrivate=False)
	entries = entries.order_by('-date')
	for entry in entries:
		entry.text=entry.text.replace('\n','<br />')	
	images = Image.objects.all()
	comments = Comment.objects.all().order_by('-date')
	form = CommentForm()
	
	### for map multi select
	location_choices=location_form()
	location_array=json.dumps(getLocationMap())
	return render_to_response('starter-template.html',locals(),RequestContext(request))

class CommentForm(ModelForm):
	class Meta:
		model=Comment
		widgets = {
			'text': Textarea(attrs={'class':'span6 addCommentInput'}),
			'user': TextInput(attrs={'class':'addCommentInput'}),
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
		
def delete_comment(request,pkey):
	p=request.POST
	if request.user.is_staff:
		comment=Comment.objects.get(pk=pkey)
		comment.delete()
	return HttpResponseRedirect(reverse("blog_index"))

def add_location(request):
	location_array= request.POST
	latitude=location_array["latitude"]
	longitude=location_array["longitude"]
	title=location_array["title"]
	note=location_array["note"]
	location= Location()
	if latitude!=0 and longitude!=0 and title!='':
		location.title=title
		location.latitude=latitude
		location.longitude=longitude
		location.note=note	
		location.save()
	stuff= [location.id,str(location.date.date().strftime("%m/%d/%y"))]
	return HttpResponse(json.dumps(stuff), mimetype="application/json")

def getLocationMap():
	locations=Location.objects.all().order_by('-date')
	location_array={}
	for location in locations:
		latitude=str(location.latitude)
		longitude=str(location.longitude)
		location_array[location.id]=[latitude,longitude,location.note,location.title,str(location.date.date().strftime("%m/%d/%y"))]
	return location_array
