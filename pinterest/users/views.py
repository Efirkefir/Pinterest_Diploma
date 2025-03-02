from django.shortcuts import render, get_object_or_404
from .models import Image

def profile_view(request,username):
    """
    Open profile page.
    """
    profile = get_object_or_404(Image, user__username=username)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)

# Create your views here.
