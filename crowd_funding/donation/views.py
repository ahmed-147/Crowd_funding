from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Donation, Project
# Create your views here.

#Add donation
@login_required
def add_donation(request, pk):
    # pk for project to retrive project
    if request.POST:
        project = Project.objects.filter(pk=pk).first()
        donation = Donation.objects.create(project=project, user=request.user, value=request.POST['donation'])
        return redirect('project:show_project', pk=pk)

    return redirect('project:show_project', pk=pk)
