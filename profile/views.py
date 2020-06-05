from django.shortcuts import render
from project.models import Project


def home(request):
    projects = Project.objects.all()

    return render(request, 'profile/home.html', {'projects': projects})
