from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import Register_form
from django.contrib.auth.models import User
from .models import user_profile
from django.db.models import Q
from project.models import Project
from donation.models import Donation

#from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.sites.models import Site


# Create your views here.


# login function
def user_login(request):
    # when request POST
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

    return redirect('home')


# logout function
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')



def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    else:
        return redirect('home')



# register function
def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.POST:
        data = request.POST
        form = Register_form(request.POST, request.FILES)
        if form.is_valid():
            # create new user
            valid_user = User.objects.filter(Q(username=data['username']) | Q(email=data['email']))
            if len(valid_user) > 0:
                print(valid_user)
                return render(request, "user_profile/register.html", {'form': form,
                                                                      'msg': "enter valid username or email"})
            user = User.objects.create_user(username=data['username'],
                                            first_name=data['first_name'],
                                            last_name=data['last_name'],
                                            email=data['email'],
                                            password=data['password'],
                                            )
            user.is_active = False
            user.save()
            # create new profile
            profile = user_profile.objects.create(user=user,
                                                  phone=data['phone'],
                                                  facebook_link=data['facebook_link'],
                                                  country=data['country'],
                                                  img=request.FILES['img'],
                                                  )
            if data['birth_date'] is not None:
                profile.birth_date = data['birth_date']
                profile.save()

            current_site = Site.objects.get_current()
            print(current_site.domain)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect('home')

        else:
            # redirect to the same page
            return render(request, "user_profile/register.html", {'form': form})
    else:
        form = Register_form()
        return render(request, "user_profile/register.html", {'form': form})


# show profile
def show_profile(request, pk):
    try:
        user = User.objects.filter(pk=pk).first()
        projects = Project.objects.filter(user=user)
        profile = user_profile.objects.filter(user=user).first()
        donations = Donation.objects.filter(user=user)
        if profile:
            return render(request, 'user_profile/profile.html', {'profile': profile,
                                                                 'projects': projects,
                                                                 'donations': donations})
        else:
            return redirect('home')

    except:
        return redirect('home')


# edit profile
@login_required
def edit_profile(request, pk):
    try:
        if request.POST:
            # pk for profile not user
            data = request.POST
            profile = user_profile.objects.filter(pk=pk).first()
            if profile.user.pk == request.user.pk:
                if request.FILES.get('img1'):
                    profile.img = request.FILES.get('img1')
                if data['first_name']:
                    profile.user.first_name = data['first_name']
                if data['last_name']:
                    profile.user.last_name = data['last_name']
                if data['phone']:
                    profile.phone = data['phone']
                if data['country']:
                    profile.country = data['country']
                if data['facebook_url']:
                    profile.facebook_link = data['facebook_url']
                if data['birth_date']:
                    profile.birth_date = data['birth_date']
                profile.user.save()
                profile.save()

            return redirect('user_profile:show_profile', pk=profile.user.pk)
        else:

            return redirect('home')

    except:

        return redirect('home')

