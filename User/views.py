from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import LoginForm, RegistrationForm, UpdateProfileForm
from .models import UserInformation

import pytz
from django.utils import timezone


def registration(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            plan = form.cleaned_data.get('plan')
            phone_number = form.cleaned_data.get('phone_number')

            if password != confirm_password:
                messages.warning(request, 'Entered passwords do not match.')
                return redirect('register')
                
            if len(phone_number) != 10 or not phone_number.isdigit():
                messages.warning(request, 'Kindly enter a valid phone number.')
                return redirect('register')

            user = User(
                first_name=first_name,
                last_name=last_name,
                username=email,
                email=email,
            )

            user.set_password(password)
            user.save()

            user_information = UserInformation(
                user=user,
                plan=plan,
                phone_number=phone_number
            )
            user_information.save()

            request.session['logged_in'] = True
            request.session['id'] = user.pk
            
            messages.success(request, 'Registration succesful.')
            return redirect('homepage')
        else:
            messages.warning(request, form.errors)
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        "form": form
    }

    return render(request, 'User/registration.html', context)


def login_auth(request):
    if "id" in request.session.keys():
        return redirect('homepage')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(username=email, password=password)

            if user is not None:
                request.session['logged_in'] = True
                request.session['id'] = user.pk

                return redirect('homepage')
            else:
                messages.warning(
                    request, "Invalid Credentials.")
                return redirect('login')
        else:
            messages.warning(request, form.errors)
            return redirect('login')
    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, 'User/login.html', context)


def logout_auth(request):
    logout(request)

    messages.success(request, 'Successfully logged out.')
    return redirect('login')


def homepage(request):
    try:
        if not request.session["logged_in"]:
            messages.warning(request, 'Kindly login before accessing the service.')  
            return redirect('login')
    except:
        messages.warning(request, 'Kindly login before accessing the service.')
        return redirect('login')

    tz_str = request.COOKIES.get('timezone')
    if tz_str:
        timezone.activate(pytz.timezone(tz_str))
    
    user_id = request.session["id"]
    user = User.objects.get(pk=user_id)
    user_information = UserInformation.objects.get(user=user)

    data = {
        "name": user.first_name + " " + user.last_name,
        "email": user.email,
        "phone_number": user_information.phone_number,
        "plan": user_information.plan
    }
    
    return render(request, 'User/home.html', data)


def update_profile(request):
    try:
        if not request.session["logged_in"]:
            messages.warning(request, 'Kindly login before accessing the service.')  
            return redirect('login')
    except:
        messages.warning(request, 'Kindly login before accessing the service.')
        return redirect('login')

    user_id = request.session["id"]
    user = User.objects.get(pk=user_id)
    user_information = UserInformation.objects.get(user=user)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            plan = form.cleaned_data.get('plan')
            phone_number = form.cleaned_data.get('phone_number')
                
            if len(phone_number) != 10 or not phone_number.isdigit():
                messages.warning(request, 'Kindly enter a valid phone number.')
                return redirect('update')

            
            user.first_name = first_name
            user.last_name = last_name
            user.username = email
            user.email = email
            user.save()

            user_information.plan = plan
            user_information.phone_number = phone_number
            user_information.save()
            
            messages.success(request, 'Profile successfully updated.')
            return redirect('homepage')
        else:
            messages.warning(request, form.errors)
            return redirect('update')
    else:
        form = UpdateProfileForm(initial={'first_name': user.first_name,'last_name': user.last_name,'email': user.email,'phone_number': user_information.phone_number,'plan': user_information.plan})

    context = {
        "form": form
    }

    return render(request, 'User/update_profile.html', context)