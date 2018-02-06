from django.shortcuts import render
from .models import Deck
# Create your views here.
def home(request):
    '''
    Render the FLASHCARD app home template
    '''
    qs = Deck.objects.all
    context = {}
    return render(request, 'flashcards/home.html')
