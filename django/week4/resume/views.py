from django.shortcuts import render
from .models import Resume, Education, Experience


def resume(request):
    """
    renders the resume page from resume app
    """
    resume = Resume.objects.all()

    return render(request, "resume/resume.html",
        context={"resume": resume})
