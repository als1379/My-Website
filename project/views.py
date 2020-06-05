from django.shortcuts import render, get_object_or_404
from .models import Project


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/project.html', {'project': project})
