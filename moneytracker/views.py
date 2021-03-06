from django.shortcuts import render_to_response
from django.template.defaultfilters import stringfilter
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from moneytracker.models import Expense,Month,Category,PayMethod
from django.forms import ModelForm,Textarea,TextInput
from django.db.models import Sum
import operator
import navbarbuilder
import json
import os


def addPayment(request):
	menu = navbarbuilder.get_navbar(request)	
	if request.user.is_staff:
		month = Month.objects.order_by('-id')[0]
		percentageUsed = round(100*month.total()/month.available,1)
		form = expense_form()
		#get top 3 expenses
		topExpenses=Expense.objects.order_by('-id')[0:3]
		if request.method == 'POST':
			requestedForm = expense_form(request.POST)
			if requestedForm.is_valid():
				requestedForm.save()
			else:
				form=requestedForm
		catMap=getCategoryPaymethodMap()
		return render_to_response('addPayment.html',locals(),RequestContext(request))
	else:
		return render_to_response('auth.html',locals(),RequestContext(request))
		
def expenseReport(request):
	menu = navbarbuilder.get_navbar(request)	
	if request.user.is_staff:
		months = Month.objects.order_by('-id')
		if request.method=='POST':
			selectedmonth=months.get(id=request.POST['months'])
		else:
			selectedmonth = months[0]
		categories=Category.objects.all()
		expenses = Expense.objects.filter(month=selectedmonth)
		separate_expenses = {}
		separate_totals = {}
		for category in categories:
			separate_expenses[category.title]=expenses.filter(has_category=category)
			separate_totals[category.title]=expenses.filter(has_category=category).aggregate(total=Sum('amount'))['total'];
		return render_to_response('expenseReport.html',locals(),RequestContext(request))
	else:
		return render_to_response('auth.html',locals(),RequestContext(request))

def getCategoryPaymethodMap():
	cats=Category.objects.all()
	catMap={}
	for x in cats:
		allCategory=Expense.objects.filter(has_category=x).values_list('has_payMethod',flat=True)
		payMethods={}
		for y in allCategory:
			if y in payMethods:
				payMethods[y]=payMethods[y]+1
			else:
				payMethods[y]=1
		catMap[x.pk]=max(payMethods.iteritems(), key=operator.itemgetter(1))[0]	
	return catMap

class expense_form(ModelForm):
	class Meta:
		model = Expense

def add_expense(request, pk):
	return HttpResponseRedirect(reverse("blog_index"))

