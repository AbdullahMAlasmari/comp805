from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    greeting = "Flash Courses"
    # a dictionary with a keyword 'our_greeting' mapping to the variable greeting defined above.
    context = {'our_greeting':greeting}
    return render(request, 'home.html', context)
