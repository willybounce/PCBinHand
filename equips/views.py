from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import EquipInfo,Attr

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return render(request,'equips/index.html',)
	else:
		form = UserCreationForm()
	return render(request,'signup.html',{'form' : form})

def logout(request):
	return render(request,'registration/logged_out.html',)

def index(request):
	latest_equips_list = EquipInfo.objects.order_by('-date_added')[:5]
	context = {'latest_equips_list' : latest_equips_list}
	return render(request,'equips/index.html',context)

def about(request):
	return render(request,'equips/about.html',)

def physics(request):
	physics_equips_list = EquipInfo.objects.filter(equip_dept__startswith='physics')
	context = {'physics_equips_list' : physics_equips_list}
	return render(request,'equips/pdetails.html',context)

def chemistry(request):
	chemistry_equips_list = EquipInfo.objects.filter(equip_dept__startswith='chemistry')
	context = {'chemistry_equips_list' : chemistry_equips_list}
	return render(request,'equips/cdetails.html',context)

def biology(request):
	biology_equips_list = EquipInfo.objects.filter(equip_dept__startswith='biology')
	context = {'biology_equips_list' : biology_equips_list}
	return render(request,'equips/bdetails.html',context)

def detail(request,equip_id):
	equipment = get_object_or_404(EquipInfo,pk=equip_id)
	return render(request,'equips/detail.html',{'equipment':equipment})

def results(request,equip_id):
	equipment = get_object_or_404(EquipInfo,pk=equip_id)
	return render(request,'equips/results.html',{'equipment':equipment})

def add_in_wishlist(request,equip_id):
	equipment = get_object_or_404(EquipInfo,pk=equip_id)
	try:
		selected_choice = equipment.attr_set.get(pk=request.POST['choice'])
	except(KeyError,Attr.DoesNotExist):
		return render(request,'equips/detail.html',{'equipment':equipment , 'error_message':"You didn't select a choice.", })
	else:
		selected_choice.in_wishlist+=1
		# equipment.no_in_stock-=1
		selected_choice.save()
		# equipment.save()
		return HttpResponseRedirect(reverse('equips:results',args=(equipment.id,)))
