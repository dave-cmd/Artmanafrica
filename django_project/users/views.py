from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.core.mail import send_mail
import threading


# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form, 
        'title': 'Profile'
    }

    current_user = request.user

    if request.method == 'POST':
        name = request.POST['name'] 
        email = request.POST['email']
        message = request.POST['message']
        def threader(name, message, sender):
            send_mail(name, message, current_user.email, ['artmanafrica@gmail.com'], fail_silently=False)

        t1 = threading.Thread(target=threader, args=(name+', '+email,message,current_user.email))
        t1.start()
        messages.success(request, f'Mail sent!')

    return render(request, 'users/profile.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, (f'Account created for {username}!'))
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Registration'})


