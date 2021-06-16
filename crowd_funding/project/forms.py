from django import forms
from category.models import Category
import datetime
class Project_form(forms.Form):
    title = forms.CharField(label=False, max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Enter a title for your Project',
                                                          'name': "title"
                                                          }))



    target = forms.IntegerField(label=False,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'min': 5000,
                                                              'placeholder': "Enter the amount you want to reach",
                                                              'type': "number",
                                                              'name': "target",
                                                              }))

    MYQUERY = Category.objects.values_list('pk', 'name')
    category = forms.CharField(label=False,
                               widget=forms.Select(attrs={'class': 'form-control',
                                                          'name': "category",
                                                          },
                                                   choices=(*MYQUERY,)))

    start_date = forms.DateField(label=False,
                                 required=True,
                                 initial=datetime.datetime.now(),
                                 widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input',
                                                               'type': 'date',
                                                               'name': 'start_date',
                                                               }), )
    end_date = forms.DateField(label=False,
                               required=True,
                               initial=datetime.datetime.now(),
                               widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input',
                                                             'type': 'date',
                                                             'name': 'end_date',
                                                             }), )

    """details = forms.CharField(label=False,
                              widget=forms.Textarea(attrs={'rows': 3,
                                                           'cols':50,
                                                           'placeholder': "Mention some details of your project",
                                                           'name': 'details',
                                                           }))
    tags = forms.CharField(label=False,
                           widget=forms.Textarea(attrs={'rows': 3,
                                                        'placeholder': "Tage1,Tage2 (Nots: without spaces)",
                                                        'name': 'tags',
                                                        'id': "inputDetails"
                                                        }))

    img = forms.ImageField(label=False,
                           widget=forms.FileInput(attrs={'type': "file",
                                                         'class': "custom-file-input",
                                                         'id': "inputImages",
                                                         'multiple': True
                                                         }))

"""