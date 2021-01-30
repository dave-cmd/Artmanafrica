from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ArtForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.core.mail import send_mail
import threading


def home(request):
    posts_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'posts': Post.objects.all().order_by('-timestamp'),
        'title': 'Home',
        'page_obj': page_obj
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

    return render(request, 'gallery/home.html', context)

def about(request):
    context = {
        'title': 'About'}
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
        
    return render( request, 'gallery/about.html', context)

@login_required(login_url='login')
def gallery_post(request):
    user =  request.user

    form = ArtForm(instance=User)
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post sucessful!')
            return redirect('gallery')
            

    context = {
        'form': form,
        'title': 'Gallery Post'
    }
    
    return render( request, 'gallery/gallery.html', context)




