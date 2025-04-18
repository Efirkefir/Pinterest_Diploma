from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .models import Image, Category
from .forms import ImageForm, RegisterForm

def home(request):
    """
    Displays the main page of the application.
    """
    return render(request, 'images/home.html')

class CustomLoginView(LoginView):
    template_name = 'images/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

@login_required
def profile(request):
    return render(request, 'images/profile.html')

def register(request):
    """
    Responsible for registering new users.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('image_list')
    else:
        form = RegisterForm()
    return render(request, 'images/register.html', {'form': form})

def upload_image(request):
    """
    Responsible for uploading images by users
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'images/upload.html', {'form': form})

def image_list(request):
    """Responsible for displaying the list of images"""
    images = Image.objects.filter(deleted=False)
    return render(request, 'images/list.html', {'images': images})

@login_required
def edit_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if image.user != request.user:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("Вы не можете редактировать это изображение")
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm(instance=image)
    return render(request, 'images/edit.html', {'form': form})

@login_required
def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if image.user != request.user:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("Вы не можете ")
    image.delete()
    return redirect('image_list')


