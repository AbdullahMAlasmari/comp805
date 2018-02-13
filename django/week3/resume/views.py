from django.shortcuts import render
from .models import Education, Experience
# Create your views here.

def home(request):
    """
    renders the resume home template
    """
    name = "Abdullah Alasmari"
    address = "1205 Hancock St, Quincy, MA, 02169"
    phone = "617 784 3387"
    email = "alasmari_0007@hotmail.com"
    skills = ["Django","Python"]
    context = {}
    educations = Education.objects.order_by('degree')
    experiences = Experience.objects.order_by('title')
    context = {'my_education':educations,'my_experiences':experiences,
    'my_name':name,'my_addr':address,'my_phone':phone,"my_email":email,
    "my_skills":skills}
    return render(request,'resume/home.html',context)
