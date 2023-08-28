from django.urls import path,include
from .views import UserRegisterView, UserEditView, PasswordsChangeView

from django.contrib.auth import views as auth_views ## For edit password function

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile',UserEditView.as_view(),name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html'))
    path('password/', PasswordsChangeView.as_view(template_name = 'registration/change_password.html'))
    
]
