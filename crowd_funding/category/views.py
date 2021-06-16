from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .forms import Category_form
from .models import Category
# Create your views here.


@login_required
@permission_required('is_superuser')
def add_category(request):
    if request.POST:
        data = request.POST
        form = Category_form(request.POST)
        if form.is_valid():
            category = Category.objects.create(name=data['name'], user=request.user)
            form = Category_form()
            return render(request, "category/add_category.html", {'good_alert': "Category Created successfully you can create another category",
                                                                  'form': form})
        else:
            # redirect to the same page
            return render(request, "category/add_category.html", {'bad_alert': "failed to create category try again",
                                                                  'form': form})
    else:
        form = Category_form()
        return render(request, "category/add_category.html", {'form': form})



@login_required
@permission_required('is_superuser')
def edit_category(request, pk):
    if request.POST:
        data = request.POST
        form = Category_form(request.POST)
        if form.is_valid():
            category = Category.objects.filter(pk=pk).first()
            category.name = data['name']
            category.save()
            return render(request, "category/edit_category.html", {'good_alert': "Category updated successfully",
                                                                   'form':form})
        else:
            # redirect to the same page
            return render(request, "category/edit_category.html", {'bad_alert': "Failed to update category",
                                                                   'form':form})
    else:
        category = Category.objects.filter(pk=pk).first()
        form = Category_form()
        return render(request, "category/edit_category.html", {'form': form})



def show_categories(request):
    categories = Category.objects.all()
    return render(request, 'category/show_categories.html', {'categories': categories})


