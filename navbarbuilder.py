from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
import os

def get_navbar(request):
	menu = {}
	if request.user.is_staff:
		menu['Blog']="/"
		menu['Create Expense']="/addPayment"
		menu['Admin']="/admin"
		menu['View Report']="/expenseReport"
	else:
		menu['Blog']="/"
	return menu
