from django.urls import path
from .views import home, CustomLoginView, CustomLogoutView, profile, register, upload_image, image_list, edit_image, delete_image


urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('upload/', upload_image, name='upload_image'),
    path('images/', image_list, name='image_list'),
    path('edit/<int:pk>/', edit_image, name='edit_image'),
    path('delete/<int:pk>/', delete_image, name='delete_image'),
]

