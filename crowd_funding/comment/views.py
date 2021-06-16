from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from project.models import Project
from .models import Comment
from django.db.models import Q
# Create your views here.
@login_required
def add_comment(request, pk):
    #pk of the project not comment
    if request.POST:
        project = Project.objects.filter(pk=pk).first()
        if project:
            Comment.objects.create(project=project,
                                   text=request.POST['comment'],
                                   user=request.user)
            return redirect('project:show_project', pk=pk)
        else:
            return redirect('project:show_project', pk=pk)
    else:
        return redirect('project:show_project', pk=pk)


@login_required
def report_comment(request, pk, projectPk):
    #pk of comment
    project = Project.objects.filter(Q(user=request.user) & Q(pk=projectPk)).first()
    comment = Comment.objects.filter(Q(pk=pk) & Q(project=project)).first()
    if comment:
        comment.delete()
        return redirect('project:show_project', pk=projectPk)

    return redirect('project:show_project', pk=projectPk)