from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   '''
   Renders flashcard app home page
   '''
   return HttpResponse('Welcome to the flashcard app')
