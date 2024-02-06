from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import CustomUser, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def register_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('mobilenumber')
        user_password = request.POST.get('password')
        user_obj = CustomUser.objects.filter(email = email)
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        

        # print(name, email, mobilenumber, user_password)

        # Create a new CustomUser object and save it to the database
        try:
            user_obj = CustomUser.objects.create_user(
                name=name, email=email, mobilenumber=mobilenumber
                )
            user_obj.set_password(user_password)
            user_obj.save()
            
            # send_mail(
            #     "Activation Link",
            #     "127.0.0.1/account_activation/",
            #     settings.EMAIL_HOST_USER,
            #     [email],
            #     fail_silently=False,
            # )
        except Exception as eddsd:
            print(eddsd)

        messages.success(request,"An Email Has Been Send To You. Please Activate Your Account From There.   ")
        return redirect('login')

    return render(request, 'registration/signup.html')


def login_page(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('name')
        password = request.POST.get('password')

        try:
            authenticated_user = authenticate(
                request, email=username_or_email, password=password)

            if authenticated_user is None:
                authenticated_user = authenticate(
                    request, mobilenumber=username_or_email, password=password)

            if authenticated_user is not None:
                auth_login(request, authenticated_user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials')
        except Exception as e:
            
            messages.error(request, f'Login failed. {str(e)}')

    return render(request, 'registration/login.html')


@login_required(login_url='/error')
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url='/login')
def home(request):
    return render(request, 'index.html')


def error(request):
    return render(request, 'registration/error.html')


@login_required(login_url='/error')
def password_change(request):
    # if request.method == "POST":
    #     old_password = request.POST.get('old_passwrod')
    #     new_password = request.POST.get('new_password')
    #     cnf_new_pass =  request.POST.get('cnf_new_pass')

    #     print(request.user.email)

    #     return redirect('home')
    return render(request, 'rergistration/password_change.html')


def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')