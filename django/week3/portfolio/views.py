from django.shortcuts import render

def home(request):
	'''
	Renders home page
	'''
	context = {}
	return render(request,'home.html',context)

def resume(request):
	'''
	Renders resume page
	'''
	name = "abdullah"
	address = "1205 hancock st, Quincy"
	phone = "6177843387"
	email = "alasmari_0007@hotmai.com"
	skills = ["Java"]
	context = {'my_name':name,'my_addr':address,'my_phone':phone,"my_email":
	email,"my_skills":skills}
	return render(request,'resume.html',context)

def portfolio(request):
	'''
	Renders portfolio page
	'''
	context = {}
	return render(request,'portfolio.html',context)

def contact(request):
	'''
	Renders contact page
	'''
	context = {}
	return render(request,'contact.html',context)
