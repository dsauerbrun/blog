# Create your views here.
from django.contrib.auth import authenticate,login
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect

def login_user(request):
    state = "nada"
    c = {}
    c.update(csrf(request))
    username=password=''
    if request.method == 'POST':
	print "not much"
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
	    return HttpResponseRedirect('/home')
        else:
	    return HttpResponseRedirect('/login')
    else:
	state="hello"
    return render_to_response('auth.html',{'state':state,'username':username},RequestContext(request))
