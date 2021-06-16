from django.shortcuts import render, redirect
from .models import Rate, Project
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


#Rate Project (add rate and update it)
@login_required
def add_rate(request, pk):
    if request.POST:
        if 'rating' not in request.POST:
            return redirect('project:show_project', pk=pk)
        project = Project.objects.filter(pk=pk).first()
        rate = Rate.objects.filter(Q(project=project) & Q(user=request.user)).first()
        # if user create rate in this project update it
        if rate:
            project.sum_rate -= rate.rate
            project.sum_rate += int(request.POST['rating'])
            rate.rate = int(request.POST['rating'])
            project.avg_rate = project.sum_rate / project.count_rated_user
            project.save()
            rate.save()
        else:
            # if user rate new project
            rate = Rate.objects.create(rate=request.POST['rating'], user=request.user, project=project)
            project.sum_rate += int(request.POST['rating'])
            project.count_rated_user += 1
            project.avg_rate = project.sum_rate / project.count_rated_user

            project.save()

    return redirect('project:show_project', pk=pk)
