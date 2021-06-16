from django import forms
import datetime
class Register_form(forms.Form):
    username = forms.CharField(label=False, max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Username',
                                                             }))
    first_name = forms.CharField(label=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'First Name',
                                                               }))
    last_name = forms.CharField(label=False,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Last Name',
                                                              }))
    email = forms.EmailField(label=False,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Email',
                                                           }))
    password = forms.CharField(label=False, max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password',
                                                                 }))
    confirm_password = forms.CharField(label=False, max_length=50,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Confirm password',
                                                                         }))
    phone = forms.CharField(label=False, max_length=11,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Phone',
                                                          'pattern': '^01[0-2]\d{1,8}$',
                                                          }))
    img = forms.ImageField(label='Enter Photo(.PNG , .JPG)',
                           widget=forms.FileInput(attrs={'class': 'form-control',
                                                         }))

    birth_date = forms.DateField(label='Birth date', required=False,
                                 widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input',
                                                               'type': 'date',
                                                               }), )
    facebook_link = forms.URLField(label=False, required=False, max_length=200,
                                   widget=forms.URLInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Facebook link',
                                                                }))

    country = forms.CharField(label=False, required=False, max_length=20,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Country',
                                                            }))

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
