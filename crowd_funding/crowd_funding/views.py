from django.shortcuts import render
from project.models import Project, Category
from tag.models import proiect_tag, Tag

def home(request):
    # All Category
    categories = Category.objects.all().order_by('pk')[:5]

    # top rated
    toprated5_projects = Project.objects.all().order_by('-avg_rate', '-pk')[:5]
    # to get featured project
    featured4_projects = Project.objects.filter(featured=True).order_by('-pk')[1:5]
    # to get featured first project
    featured_first_project = Project.objects.filter(featured=True).order_by('-pk').first()

    # to get latest 5 project
    latest5_projects = Project.objects.all().order_by('-pk')[:5]
    context = {
        'categories': categories,
        'latest5_projects': latest5_projects,
        'featured4_projects': featured4_projects,
        'featured_first_project': featured_first_project,
        'toprated5_projects': toprated5_projects,
    }
    return render(request, 'index.html', context)


def show_projects(request):
    all_categories = Category.objects.all()
    if request.POST:
        print(request.POST)
    else:

        # if search by tag and title
        if request.GET.get('q'):
            #tags = Tag.objects.filter(name__icontains=request.GET.get('q'))
            #print(tags)
            #project_tag = proiect_tag.objects.all()
            #print(project_tag)
            #for tag in tags:
               # project_tag = project_tag.filter(tag=tag)
                #print(project_tag)
            #print(project_tag)
            projects = Project.objects.filter(title__icontains=request.GET.get('q'))
            context = {
                'projects': projects,
                'categories': all_categories,
            }
            return render(request, 'search_projects.html', context)

        # search by category pk
        if request.GET.get('search'):
            category = Category.objects.filter(pk=int(request.GET.get('search'))).first()
            projects = Project.objects.filter(category=category)
            context = {
                'projects': projects,
                'categories': all_categories,
            }

            return render(request, 'search_projects.html', context)


        #order by featured project
        if request.GET.get('featured'):
            projects = Project.objects.filter(featured=True).order_by('-pk')
            context = {
                'projects': projects,
                'categories': all_categories,
            }
            return render(request, 'search_projects.html', context)
        #order by last project
        if request.GET.get('last'):
            projects = Project.objects.all().order_by('-pk')
            context = {
                'projects': projects,
                'categories': all_categories,
            }
            return render(request, 'search_projects.html', context)
    context = {
        'categories': all_categories,
    }
    return render(request,'search_projects.html', context)
